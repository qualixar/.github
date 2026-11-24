#!/usr/bin/env python3
"""Render the qualixar org and varun369 profile READMEs from data/products.json.

Live numbers (stars, releases, creation dates, npm and PyPI downloads) are fetched
at build time. Every row also carries shields.io badges, so stars and versions stay
current between builds. If an API call fails, the last good value from
data/stats.json is used, so a README never shows a blank or a zero by accident.

Usage:
  python scripts/build_readmes.py --org profile/README.md
  python scripts/build_readmes.py --personal ../varun369/README.md
  python scripts/build_readmes.py --offline ...   # cache only, no network (tests)

Standard library only, so the GitHub Action needs no install step.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "data" / "products.json"
STATS = ROOT / "data" / "stats.json"
ORG = "qualixar"
UA = {"User-Agent": "qualixar-readme-builder", "Accept": "application/vnd.github+json"}


# ---------------------------------------------------------------- fetching

def _get_json(url: str) -> object | None:
    headers = dict(UA)
    token = os.environ.get("GITHUB_TOKEN")
    if token and "api.github.com" in url:
        headers["Authorization"] = f"Bearer {token}"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=20) as r:
            return json.load(r)
    except urllib.error.HTTPError as exc:
        if not (exc.code == 404 and url.endswith("/releases/latest")):  # no release yet is normal
            print(f"warn: {url}: {exc}", file=sys.stderr)
        return None
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        print(f"warn: {url}: {exc}", file=sys.stderr)
        return None


def _repo_stats(repo: str) -> dict | None:
    info = _get_json(f"https://api.github.com/repos/{repo}")
    if not isinstance(info, dict) or "stargazers_count" not in info:
        return None
    rel = _get_json(f"https://api.github.com/repos/{repo}/releases/latest")
    tag = rel.get("tag_name") if isinstance(rel, dict) else None
    return {"stars": info["stargazers_count"], "created": info["created_at"][:10],
            "pushed": info["pushed_at"][:10], "release": tag}


def _org_stars() -> int | None:
    total, page = 0, 1
    while True:
        repos = _get_json(f"https://api.github.com/orgs/{ORG}/repos?per_page=100&type=public&page={page}")
        if not isinstance(repos, list):
            return None
        total += sum(r["stargazers_count"] for r in repos if not r.get("fork"))
        if len(repos) < 100:
            return total
        page += 1


def _downloads(npm: str, pypi: str, today: dt.date) -> dict:
    out: dict = {}
    n = _get_json(f"https://api.npmjs.org/downloads/point/2015-01-10:{today.isoformat()}/{npm}")
    if isinstance(n, dict) and isinstance(n.get("downloads"), int):
        out["npm"] = n["downloads"]
    p = _get_json(f"https://pepy.tech/api/v2/projects/{pypi}")
    if isinstance(p, dict) and isinstance(p.get("total_downloads"), int):
        out["pypi"] = p["total_downloads"]
    return out


def collect(reg: dict, offline: bool, today: dt.date) -> dict:
    """Return stats, falling back field by field to the cached file."""
    cache = json.loads(STATS.read_text()) if STATS.exists() else {"repos": {}}
    if offline:
        return cache
    repos = dict(cache.get("repos", {}))
    for p in reg["products"]:
        for repo in [p["repo"], *p.get("includes", [])]:
            fresh = _repo_stats(repo)
            if fresh:
                repos[repo] = fresh
    stats = {"repos": repos, "built": today.isoformat()}
    stats["org_stars"] = _org_stars() or cache.get("org_stars")
    dl = _downloads(reg["hero"]["npm"], reg["hero"]["pypi"], today)
    stats["downloads"] = {**cache.get("downloads", {}), **dl}
    STATS.write_text(json.dumps(stats, indent=2, sort_keys=True) + "\n")
    return stats


# ---------------------------------------------------------------- rendering

def _compact(n: int) -> str:
    """Round DOWN so a '+' after the number is always true (201,580 -> '201k')."""
    if n >= 10000:
        return f"{n // 1000}k"
    if n >= 1000:
        return f"{n // 100 / 10:.1f}k"
    return str(n)


HERO_SVG = ROOT / "assets" / "qualixar-readme-hero.svg"
_SVG_COUNTS = re.compile(r">\d+ CORE PRODUCTS(\s+•\s+)\d+ PUBLIC ARXIV PREPRINTS<")


def patch_hero_svg(reg: dict, path: Path = HERO_SVG) -> bool:
    """Keep the counts drawn inside the hero image in step with the registry."""
    if not path.exists():
        return False
    svg = path.read_text()
    new = _SVG_COUNTS.sub(
        lambda m: f">{product_count(reg)} CORE PRODUCTS{m.group(1)}{len(reg['papers'])} PUBLIC ARXIV PREPRINTS<", svg)
    if new != svg:
        path.write_text(new)
    return new != svg


def _badges(repo: str, release: str | None) -> str:
    stars = (f"![stars](https://img.shields.io/github/stars/{repo}?style=flat&label=%E2%98%85"
             f"&color=f5b301&labelColor=2b2b2b)")
    if not release:
        return stars
    ver = (f"![release](https://img.shields.io/github/v/release/{repo}?style=flat&label="
           f"&color=3b82f6&labelColor=2b2b2b)")
    return f"{stars} {ver}"


def _included_stars(repo: str) -> str:
    short = repo.split("/")[1]
    return (f"[![{short} stars](https://img.shields.io/github/stars/{repo}?style=flat"
            f"&label=%E2%98%85%20{short}&color=f5b301&labelColor=2b2b2b)](https://github.com/{repo})")


def _paper_count(reg: dict, slug: str) -> int:
    return sum(1 for x in reg["papers"] if x["product"] == slug)


def product_count(reg: dict) -> int:
    return sum(1 + len(p.get("includes", [])) for p in reg["products"])


def split_tiers(reg: dict, stats: dict, today: dt.date) -> tuple[list, list, list]:
    window = dt.timedelta(days=reg["new_window_days"])
    flagship, new, core = [], [], []
    for p in reg["products"]:
        created = stats["repos"].get(p["repo"], {}).get("created")
        if p["tier"] == "flagship":
            flagship.append(p)
        elif created and today - dt.date.fromisoformat(created) <= window:
            new.append(p)
        else:
            core.append(p)
    new.sort(key=lambda p: stats["repos"][p["repo"]]["created"], reverse=True)
    return flagship, new, core


def _row(reg: dict, stats: dict, p: dict, shipped: bool = False) -> str:
    s = stats["repos"].get(p["repo"], {})
    papers = _paper_count(reg, p["slug"])
    proof = _badges(p["repo"], s.get("release"))
    for r in p.get("includes", []):
        # a bundled repo gets its own linked star badge, so it can be starred from here
        proof += f" {_included_stars(r)}"
    if papers:
        proof += f"<br><sub>{papers} paper{'s' if papers > 1 else ''}</sub>"
    if shipped and s.get("created"):
        when = dt.date.fromisoformat(s["created"]).strftime("%d %b %Y").lstrip("0")
        proof += f"<br><sub>shipped {when}</sub>"
    repos = [p["repo"], *p.get("includes", [])]
    if len(repos) > 1:
        # a bundle row: every repo gets its own link
        name = "**" + " + ".join(f"[{r.split('/')[1]}](https://github.com/{r})" for r in repos) + "**"
    else:
        name = f"**[{p['name']}](https://github.com/{p['repo']})**"
    meta = f"<sub>{p['area']} · [Start →]({p['start']})</sub>"
    return f"| {name}<br>{meta} | {p['line']} | {proof} |"


def table(reg: dict, stats: dict, rows: list, shipped: bool = False) -> str:
    head = "| Product | What it does | Proof |\n| --- | --- | --- |"
    return "\n".join([head, *(_row(reg, stats, p, shipped) for p in rows)])


def hero(reg: dict, stats: dict) -> str:
    h = reg["hero"]
    dl = stats.get("downloads", {})
    total = (dl.get("npm") or 0) + (dl.get("pypi") or 0)
    count = f"**{_compact(total)}+ downloads** across npm and PyPI. " if total else ""
    repo = f"{ORG}/{h['slug']}"
    badges = " ".join([
        f"[![stars](https://img.shields.io/github/stars/{repo}?style=for-the-badge&label=stars&color=f5b301&labelColor=2b2b2b)](https://github.com/{repo})",
        f"[![npm](https://img.shields.io/npm/dt/{h['npm']}?style=for-the-badge&label=npm&color=cb3837&labelColor=2b2b2b)](https://www.npmjs.com/package/{h['npm']})",
        f"[![pypi](https://img.shields.io/pepy/dt/{h['pypi']}?style=for-the-badge&label=pypi&color=3775a9&labelColor=2b2b2b)](https://pypi.org/project/{h['pypi']}/)",
        f"[![release](https://img.shields.io/github/v/release/{repo}?style=for-the-badge&label=release&color=3b82f6&labelColor=2b2b2b)](https://github.com/{repo}/releases)",
    ])
    return (f"### ⭐ [SuperLocalMemory](https://github.com/{repo}): the flagship\n\n"
            f"{h['line']} {count}Backed by {_paper_count(reg, h['slug'])} arXiv preprints.\n\n"
            f"{badges}\n\n```bash\n{h['install']}\n```")


def papers_block(reg: dict, names: dict) -> str:
    rows = "\n".join(f"| {x['title']} | [{x['arxiv']}](https://arxiv.org/abs/{x['arxiv']}) | {names.get(x['product'], '')} |"
                     for x in reg["papers"])
    return (f"<details>\n<summary><b>All {len(reg['papers'])} research papers</b> (public arXiv preprints)</summary>\n\n"
            f"| Paper | arXiv | Product |\n| --- | --- | --- |\n{rows}\n\n"
            "arXiv records are preprints, not peer review. Each paper states its assumptions, versions and limits.\n\n</details>")


def _stat_line(reg: dict, stats: dict, extra: str = "") -> str:
    parts = [f"**{product_count(reg)}** open-source products", f"**{len(reg['papers'])}** arXiv preprints"]
    if stats.get("org_stars"):
        parts.append(f"**{stats['org_stars']:,}** GitHub stars")
    if extra:
        parts.append(extra)
    return " · ".join(parts)


def _footer(stats: dict) -> str:
    return (f"<sub>Tables, counts and downloads refresh automatically every day from "
            f"[one product list](https://github.com/{ORG}/.github/blob/main/data/products.json). "
            f"Last build: {stats.get('built', 'n/a')}.</sub>")


def youtube_bar(reg: dict) -> str:
    """Clickable channel card (assets/youtube-banner.webp) that opens the subscribe prompt."""
    yt = reg["youtube"]
    return (f'<p align="center">\n'
            f'  <a href="{yt["url"]}?sub_confirmation=1"><img src="../assets/youtube-banner.webp" '
            f'width="560" alt="Subscribe to {yt["name"]} on YouTube"></a>\n'
            f'</p>')


LINK_BUTTONS = [
    ("website", "Website", "https://qualixar.com"),
    ("youtube", "YouTube", "https://www.youtube.com/@Qualixar-AI?sub_confirmation=1"),
    ("discussions", "Discussions", f"https://github.com/orgs/{ORG}/discussions"),
    ("research", "Research", "https://qualixar.com/research/papers"),
]


def link_buttons() -> str:
    cells = " ".join(f'<a href="{url}"><img src="../assets/btn-{key}.png" height="40" alt="{label}"></a>'
                     for key, label, url in LINK_BUTTONS)
    return f'<p align="center">\n  {cells}\n</p>'


def render_org(reg: dict, stats: dict, today: dt.date) -> str:
    flagship, new, core = split_tiers(reg, stats, today)
    names = {p["slug"]: p["name"] for p in reg["products"]}
    new_part = (f"## New this season\n\n{table(reg, stats, new, shipped=True)}\n\n" if new else "")
    return f"""<p align="center">
  <img src="../assets/qualixar-readme-hero.svg" alt="Qualixar: AI Reliability Engineering" width="100%" />
</p>

{youtube_bar(reg)}

# Qualixar: AI Reliability Engineering

Qualixar builds open-source tools that make AI agents checkable: what an agent remembers, which actions it may take, when it is allowed to say "done", and how you test something that never answers the same way twice. It is an independent research initiative by [Varun Pratap Bhardwaj](https://github.com/varun369). Every flagship ships with source, examples and, where the claim needs one, a paper.

{_stat_line(reg, stats)}

{link_buttons()}

{hero(reg, stats)}

## Flagship products

{table(reg, stats, flagship)}

{new_part}## Toolkit

{table(reg, stats, core)}

## Research

{papers_block(reg, names)}

## Community

Ask setup questions and propose workflows in [Discussions](https://github.com/orgs/{ORG}/discussions). Report reproducible bugs in the product's own issue tracker, and follow each repository's security policy for vulnerabilities. See the [community guide](https://github.com/{ORG}/.github/blob/main/COMMUNITY.md).

{_footer(stats)}
"""


def render_personal(reg: dict, stats: dict, today: dt.date) -> str:
    flagship, new, _ = split_tiers(reg, stats, today)
    person = reg["person"]
    links = " · ".join(f"[{t}]({u})" for t, u in person["links"])
    names = {p["slug"]: p["name"] for p in reg["products"]}
    new_part = (f"### Shipped recently\n\n{table(reg, stats, new, shipped=True)}\n\n" if new else "")
    return f"""<p align="center">
  <img src="./assets/varun-readme-hero.svg" alt="Varun Pratap Bhardwaj: AI Reliability Engineering" width="100%" />
</p>

# {person['name']}

I work on **AI Reliability Engineering**: how to know an AI agent did what it says it did. That means memory you can audit, contracts an agent cannot quietly break, tests built for answers that change from run to run, and loops that end on an independent check instead of the agent's own word.

I founded [Qualixar](https://github.com/{ORG}), my independent research initiative, where I publish the tools and the papers behind them. My day job is enterprise solution architecture: {person['years']} years in IT, and {person['awards']}.

{_stat_line(reg, stats)}

{links}

{hero(reg, stats)}

### Flagship work

{table(reg, stats, flagship)}

{new_part}All {product_count(reg)} products, with setup guides, are on **[github.com/{ORG}](https://github.com/{ORG})**.

### Research

{papers_block(reg, names)}

{_footer(stats)}
"""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--org", type=Path, help="write the org profile README here")
    ap.add_argument("--personal", type=Path, help="write the personal profile README here")
    ap.add_argument("--offline", action="store_true", help="use data/stats.json only")
    ap.add_argument("--today", help="override today's date (YYYY-MM-DD), for tests")
    args = ap.parse_args(argv)
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    reg = json.loads(REGISTRY.read_text())
    stats = collect(reg, args.offline, today)
    missing = [p["repo"] for p in reg["products"] if p["repo"] not in stats.get("repos", {})]
    if missing:
        print(f"error: no stats for {missing}; run once online", file=sys.stderr)
        return 1
    if args.org:
        args.org.write_text(render_org(reg, stats, today))
        patch_hero_svg(reg)
    if args.personal:
        args.personal.write_text(render_personal(reg, stats, today))
    return 0


if __name__ == "__main__":
    sys.exit(main())
