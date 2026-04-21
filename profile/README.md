<div align="center">

# Qualixar

### Mathematically-Grounded Infrastructure for Reliable AI Agents

<br/>

**7 published papers &middot; 7 live products &middot; 10 research initiatives**

[![Website](https://img.shields.io/badge/qualixar.com-6366f1?style=for-the-badge&logo=google-chrome&logoColor=white)](https://qualixar.com)
[![arXiv](https://img.shields.io/badge/arXiv-7_papers-B31B1B?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/search/?searchtype=author&query=Bhardwaj%2C+Varun+Pratap)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0002--8726--4289-A6CE39?style=for-the-badge&logo=orcid&logoColor=white)](https://orcid.org/0009-0002-8726-4289)

---

</div>

## The Problem

2.4 million AI agents in production. Zero standard methodology for verifying they work correctly. Agents leak data, exceed budgets, drift from instructions, and fail in ways no one predicted.

Every framework helps you **build** agents. We make them **reliable** — with math, not marketing.

## Products

| Product | What It Does | Install | Links |
|---------|-------------|---------|-------|
| **[agentAssert](https://github.com/qualixar/agentassert-abc)** | Design-by-Contract for AI agents. 12 domain contracts, 293 benchmarks, &Theta;=0.9541 | `pip install agentassert-abc[yaml,math]` | [![arXiv](https://img.shields.io/badge/2602.22302-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.22302) [![Web](https://img.shields.io/badge/agentassert.com-6366f1?logo=google-chrome&logoColor=white)](https://agentassert.com) |
| **[SuperLocalMemory](https://github.com/qualixar/superlocalmemory)** | Privacy-first AI agent memory. 74.8% LoCoMo, zero cloud, Fisher-Rao retrieval | `npm i -g superlocalmemory` | [![arXiv](https://img.shields.io/badge/3_papers-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.14588) [![Web](https://img.shields.io/badge/superlocalmemory.com-06b6d4?logo=google-chrome&logoColor=white)](https://superlocalmemory.com) |
| **[SkillFortify](https://github.com/qualixar/skillfortify)** | Supply chain security for AI agent skills. 22 frameworks, 96.95% F1, 0% FP | `pip install skillfortify` | [![arXiv](https://img.shields.io/badge/2603.00195-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.00195) [![PyPI](https://img.shields.io/badge/PyPI-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/skillfortify/) |
| **[AgentAssay](https://github.com/qualixar/agentassay)** | Token-efficient regression testing for non-deterministic agents. ~83% cost reduction | `pip install agentassay` | [![arXiv](https://img.shields.io/badge/2603.02601-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.02601) |
| **[SLM MCP Hub](https://github.com/qualixar/slm-mcp-hub)** | First MCP gateway that learns. Intelligent federation, caching, cost tracking | `pip install slm-mcp-hub` | [![PyPI](https://img.shields.io/badge/PyPI-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/slm-mcp-hub/) [![npm](https://img.shields.io/badge/npm-CB3837?logo=npm&logoColor=white)](https://www.npmjs.com/package/slm-mcp-hub) |
| **[SLM Mesh](https://github.com/qualixar/slm-mesh)** | P2P communication for AI coding agents. 8 MCP tools, <100ms delivery | `npm i -g slm-mesh` | [![npm](https://img.shields.io/badge/npm-CB3837?logo=npm&logoColor=white)](https://www.npmjs.com/package/slm-mesh) |
| **[Qualixar OS](https://github.com/qualixar/qualixar-os)** | Universal agent operating system. 25 commands, every transport, every IDE | *Coming soon* | [![arXiv](https://img.shields.io/badge/2604.06392-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.06392) [![Zenodo](https://img.shields.io/badge/Zenodo-1682D4?logo=zenodo&logoColor=white)](https://zenodo.org/records/19454219) |

## Research — 7 Published Papers

| # | Paper | Venue | Product |
|---|-------|-------|---------|
| 1 | **The Living Brain** — Biologically-Inspired Forgetting, Cognitive Quantization, Multi-Channel Retrieval | [arXiv:2604.04514](https://arxiv.org/abs/2604.04514) | SuperLocalMemory V3.3 |
| 2 | **Information-Geometric Foundations** for Zero-LLM Enterprise Agent Memory | [arXiv:2603.14588](https://arxiv.org/abs/2603.14588) | SuperLocalMemory V3 |
| 3 | **Privacy-Preserving Multi-Agent Memory** with Bayesian Trust Defense | [arXiv:2603.02240](https://arxiv.org/abs/2603.02240) | SuperLocalMemory V2 |
| 4 | **Agent Behavioral Contracts** — Formal Specification and Runtime Enforcement | [arXiv:2602.22302](https://arxiv.org/abs/2602.22302) | agentAssert |
| 5 | **Formal Verification** for Agent Skill Supply Chain Security | [arXiv:2603.00195](https://arxiv.org/abs/2603.00195) | SkillFortify |
| 6 | **Token-Efficient Regression Testing** for Non-Deterministic AI Agents | [arXiv:2603.02601](https://arxiv.org/abs/2603.02601) | AgentAssay |
| 7 | **A Universal Agent Operating System** | [arXiv:2604.06392](https://arxiv.org/abs/2604.06392) | Qualixar OS |

Conference targets: NeurIPS 2026, ASE 2026, AAMAS 2027, ICSE 2027.

## In Development

| Codename | Focus Area |
|----------|-----------|
| Project Echo | Multi-agent communication degradation benchmarks |
| Project Sentinel | Reliability analysis for AI-generated code |
| Project Rewind | Time-travel debugging for autonomous agents |
| Project Aurora | Chaos engineering for AI agent systems |

## Quick Start

```bash
# Agent behavioral contracts — 12 domains, 293 benchmarks
pip install agentassert-abc[yaml,math]

# AI agent memory — works with Claude Code, Cursor, 17+ tools
npm install -g superlocalmemory

# Agent skill security — scan 22 frameworks in one command
pip install skillfortify && skillfortify scan

# MCP gateway that learns — federate 30+ MCP servers, one endpoint
pip install slm-mcp-hub && slm-mcp-hub start

# P2P agent communication — agents discover + message each other
npm install -g slm-mesh && slm-mesh start
```

## Philosophy

- Every tool is backed by **published, peer-reviewed research** — not blog posts
- We solve problems with **mathematical proofs** — not heuristics
- Every product is **open-source** and framework-agnostic
- Privacy-first: your data stays on **your machine**

## Websites

| Site | What's There |
|------|-------------|
| [**varunpratap.com**](https://varunpratap.com) | Author portfolio — all products, 7 papers, blog |
| [**agentassert.com**](https://agentassert.com) | agentAssert — benchmarks, contracts, getting started |
| [**superlocalmemory.com**](https://superlocalmemory.com) | SuperLocalMemory — architecture, integrations, research landscape |
| [**qualixar.com**](https://qualixar.com) | Platform hub — all products, documentation |

## Get Involved

- Read our [papers on arXiv](https://arxiv.org/search/?searchtype=author&query=Bhardwaj%2C+Varun+Pratap)
- Star the repos you find useful
- Open issues for bugs or feature requests
- Cite our work in your research ([BibTeX on each repo](https://agentassert.com/research))

---

<div align="center">

An independent research initiative by **[Varun Pratap Bhardwaj](https://varunpratap.com)**

Senior Manager & Solution Architect at Accenture &middot; 15 years across 6 industries

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Varun_Pratap-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/varun-pratap-bhardwaj-7ab63742)
[![X](https://img.shields.io/badge/X-@varunPbhardwaj-000000?style=flat-square&logo=x)](https://x.com/varunPbhardwaj)
[![Email](https://img.shields.io/badge/Email-varun.pratap.bhardwaj-EA4335?style=flat-square&logo=gmail)](mailto:varun.pratap.bhardwaj@gmail.com)

*We don't just identify problems in agent development. We prove solutions.*

</div>
