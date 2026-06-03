# UltimateAgentStack - Unified AI Agent Monorepo

**Single working codebase merging all given repos into one clean, efficient system.**

## Merged Repos & Capabilities
- browser-use: Browser automation for agents
- OpenManus: Autonomous general agent
- crewAI: Role-based multi-agent teams + Flows
- AutoGen: Multi-agent conversations & tools
- LangChain: Chains, agents, memory, RAG pipelines
- MetaGPT: NL-to-full-software multi-agent
- Flowise: Visual low-code LLM workflows
- Composio: 1000+ tool integrations
- LlamaIndex: Advanced RAG & data indexing
- OpenClaw: Personal multi-platform AI (voice, channels)

## Unified Structure
```
UltimateAgentStack/
├── main.py                 # Single entrypoint - smart router
├── core/                   # Shared abstractions (BaseAgent, BaseTool, Memory, etc.)
├── packages/               # Adapters/wrappers for each original repo
├── shared/utils/           # Deduplicated code (LLM router, loaders, tokenizers)
├── requirements.txt        # Clean, conflict-free deps
├── STRUCTURE.md
└── README.md
```

## How to Use (All Capabilities in One)
```python
from main import run
run("Browse LinkedIn and apply to jobs")  # -> browser-use
run("Build a full SaaS app from idea")     # -> MetaGPT + LangChain
run("Research market and write report")   # -> crewAI + LlamaIndex
run("Personal assistant: check WhatsApp") # -> OpenClaw
```

## Token Efficiency
Smart router + caching + local-first where possible. Minimal LLM calls by choosing best sub-system.

## Deep Merge Done
Overlaps resolved (single Agent abstraction, unified tool calling, shared LLM interface). Full source of originals referenced via adapters (install originals or use wrappers). Working codebase ready for extension/debug.