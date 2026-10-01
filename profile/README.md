# Qualixar — AI Reliability Engineering

Open-source tools for AI agent decisions, memory, behavioral contracts and bounded execution. Qualixar is an independent research initiative by [Varun Pratap Bhardwaj](https://www.varunpratap.com).

## Choose a starting point

| Your task | Product | Start here |
| --- | --- | --- |
| Choose a task, tool or review route from explicit options | [Jev Decision Layer](https://github.com/qualixar/jev-decision-layer) | [Decision recipes and setup](https://qualixar.com/products/jev-decision-layer) |
| Run an agent loop until an independent check passes, within declared limits | [Bounded Loops & Graphs](https://github.com/qualixar/bounded-loops) | [Keyless example and receipt verification](https://github.com/qualixar/bounded-loops/blob/main/docs/QUICK_PROOF.md) |
| Store project context and recall it across AI sessions | [SuperLocalMemory](https://github.com/qualixar/superlocalmemory) | [Install and try a local memory workflow](https://www.superlocalmemory.com) |
| Define behavioral contracts and check adapter outputs | [AgentAssert](https://github.com/qualixar/agentassert-abc) | [Released API and getting started](https://agentassert.com/getting-started/) |

Jev returns advisory decisions; its answer does not authorize an action. Bounded Loops' first keyless example uses a stub worker and real pytest checks. SuperLocalMemory's optional providers and connectors have separate network behavior. AgentAssert's small example checks a caller-supplied flag; it is not a security classifier.

## Try a product

```bash
# Bounded Loops: install a loop in your project and run its keyless example
python -m pip install bounded-loops
bl loops install bug-fix-red-green --dest ./loops
bl run loops/bug-fix-red-green --yes --run-id first-proof

# SuperLocalMemory: install, then select your operating mode explicitly
npm install -g superlocalmemory
slm setup

# AgentAssert: install the YAML and mathematical dependencies
python -m pip install 'agentassert-abc[yaml,math]'
```

For Jev, follow the [host-specific installation guide](https://github.com/qualixar/jev-decision-layer#install-and-upgrade). Check each repository's supported platforms and setup requirements before installation.

## Research and reproducible examples

Read [Qualixar's research directory](https://qualixar.com/research/papers) alongside each product's source and examples. Public arXiv papers are **preprints**; an arXiv record does not establish peer review. Mathematical results and experiment figures apply to the assumptions, datasets and versions described in each paper.

- [Bounded Loops — arXiv:2609.27871](https://arxiv.org/abs/2609.27871)
- [SuperLocalMemory 4.0 — arXiv:2608.08253v2](https://arxiv.org/abs/2608.08253v2)
- [Agent Behavioral Contracts — arXiv:2602.22302](https://arxiv.org/abs/2602.22302)

## Ask, propose, and share

Use the [Qualixar community hub](https://github.com/orgs/qualixar/discussions):

- [Q&A](https://github.com/qualixar/.github/discussions/categories/q-a): installation, configuration and usage questions.
- [Ideas](https://github.com/qualixar/.github/discussions/categories/ideas): describe a task and the workflow you want to improve.
- [Polls](https://github.com/qualixar/.github/discussions/categories/polls): help prioritize tutorials and examples.
- [Announcements](https://github.com/qualixar/.github/discussions/categories/announcements): maintainer updates and release links.
- [Show and tell](https://github.com/qualixar/.github/discussions/categories/show-and-tell): share an integration and what you observed.

Report reproducible bugs in the affected product's issue tracker. Follow the repository's published security-reporting instructions where available; do not post vulnerabilities, secrets, private prompts or customer data publicly. See the [community guide](https://github.com/qualixar/.github/blob/main/COMMUNITY.md).

If a product helps your work, starring its repository is one way to follow it. Using the tools and participating in discussions does not require a star.

## More Qualixar projects

Explore [all public repositories](https://github.com/orgs/qualixar/repositories) and the [product directory](https://qualixar.com/products) for SkillFortify, AgentAssay, SLM MCP Hub, SLM Mesh, Agent Amplifier and Qualixar OS. Consult each project's current README for availability and evidence.

[Qualixar](https://qualixar.com) · [SuperLocalMemory](https://www.superlocalmemory.com) · [AgentAssert](https://agentassert.com) · [Author and research](https://www.varunpratap.com)
