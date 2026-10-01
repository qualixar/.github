# Qualixar — AI Reliability Engineering

Open-source tools for AI agent decisions, memory, behavioral contracts and bounded execution. Qualixar is an independent research initiative by [Varun Pratap Bhardwaj](https://www.varunpratap.com).

**10 core products · 10 public arXiv preprints**

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

## All 10 products

| Product | Focus | Product page |
| --- | --- | --- |
| [Jev Decision Layer](https://github.com/qualixar/jev-decision-layer) | AI agent decision layer | [Overview](https://qualixar.com/products/jev-decision-layer) |
| [Bounded Loops](https://github.com/qualixar/bounded-loops) | Bounded AI agent loops | [Overview](https://qualixar.com/products/bounded-loops) |
| [SuperLocalMemory](https://github.com/qualixar/superlocalmemory) | Local AI agent memory | [Overview](https://qualixar.com/products/superlocalmemory) |
| [SLM MCP Hub](https://github.com/qualixar/slm-mcp-hub) | MCP gateway | [Overview](https://qualixar.com/products/slm-mcp-hub) |
| [SkillFortify](https://github.com/qualixar/skillfortify) | AI agent skill security | [Overview](https://qualixar.com/products/skillfortify) |
| [AgentAssert](https://github.com/qualixar/agentassert-abc) | AI agent behavioral contracts | [Overview](https://qualixar.com/products/agentassert) |
| [AgentAssay](https://github.com/qualixar/agentassay) | AI agent regression testing | [Overview](https://qualixar.com/products/agentassay) |
| [Agent Amplifier](https://github.com/qualixar/agent-amplifier) | AI coding-agent runtime | [Overview](https://qualixar.com/products/agent-amplifier) |
| [SLM Mesh](https://github.com/qualixar/slm-mesh) | AI agent communication | [Overview](https://qualixar.com/products/slm-mesh) |
| [Qualixar OS](https://github.com/qualixar/qualixar-os) | AI agent operating system | [Overview](https://qualixar.com/products/qualixar-os) |

This is the core product directory, not a claim that every project has the same release status, platform support or validation. Check each repository's current README before choosing a product. The four starting points above are this rollout's detailed recipe and workflow focus.

## All 10 research papers

These public arXiv records are preprints. Read each paper for its assumptions, version, experimental scope and limitations. Listing a paper beside a product does not establish that every current feature was evaluated in that paper.

| Paper | arXiv | Related project |
| --- | --- | --- |
| Bounded Loops: Pre-Run Spend Bounds, Proved Termination, and Verified Completion for Agent Harnesses | [2609.27871](https://arxiv.org/abs/2609.27871) | Bounded Loops |
| Agent Behavioral Contracts II: Certifying Compositional Reliability Without Assuming Independence | [2608.12895](https://arxiv.org/abs/2608.12895) | AgentAssert |
| SuperLocalMemory 4.0: The Governed Memory Operating System for AI Agents | [2608.08253](https://arxiv.org/abs/2608.08253) | SuperLocalMemory |
| Qualixar OS: A Universal Operating System for AI Agent Orchestration | [2604.06392](https://arxiv.org/abs/2604.06392) | Qualixar OS |
| SuperLocalMemory V3.3: The Living Brain -- Biologically-Inspired Forgetting, Cognitive Quantization, and Multi-Channel Retrieval for Zero-LLM Agent Memory Systems | [2604.04514](https://arxiv.org/abs/2604.04514) | SuperLocalMemory |
| SuperLocalMemory V3: Information-Geometric Foundations for Zero-LLM Enterprise Agent Memory | [2603.14588](https://arxiv.org/abs/2603.14588) | SuperLocalMemory |
| AgentAssay: Token-Efficient Regression Testing for Non-Deterministic AI Agent Workflows | [2603.02601](https://arxiv.org/abs/2603.02601) | AgentAssay |
| Formal Analysis and Supply Chain Security for Agentic AI Skills | [2603.00195](https://arxiv.org/abs/2603.00195) | SkillFortify |
| Agent Behavioral Contracts: Formal Specification and Runtime Enforcement for Reliable Autonomous AI Agents | [2602.22302](https://arxiv.org/abs/2602.22302) | AgentAssert |
| SuperLocalMemory: Privacy-Preserving Multi-Agent Memory with Bayesian Trust Defense Against Memory Poisoning | [2603.02240](https://arxiv.org/abs/2603.02240) | SuperLocalMemory |

[Qualixar](https://qualixar.com) · [SuperLocalMemory](https://www.superlocalmemory.com) · [AgentAssert](https://agentassert.com) · [Author and research](https://www.varunpratap.com)
