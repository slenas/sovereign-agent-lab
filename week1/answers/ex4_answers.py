"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "No matches returned. AI response was a bit out of topic commenting on what the function does. This function call will return a list of venues in Edinburgh that can accommodate at least 300 people and have vegan options. The response will include the names of the venues that match these criteria.. "

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
I changed the status of "The Albanach" to "full" in the mcp_venue_server.py file. 
This caused the search_venues tool to return only "The Haymarket Vaults" as a match for the first query. 
This demonstrates that the search_venues tool is correctly filtering venues based on their status. 
No other files needed to be updated as the MCP client automatically discovers tools at runtime.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 8 # or 0 depending on definition  # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 64   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP is a standardised, language-agnostic protocol — not just a file split.
Any compatible client (LangGraph agent, Rasa action, CLI, future mobile app) can
connect to the same server and discover its tools at runtime without knowing anything
about the other clients. A plain "separate file" is a code-organisation decision that
still requires a shared import path and a common language. MCP replaces that tight
coupling with a wire protocol: add a new @mcp.tool() to the server and every client
picks it up on the next connection with zero changes on their side. This is what lets
the LangGraph research agent and the Rasa confirmation action in this lab share a
single authoritative venue database without either one importing from the other or
being bundled together at deploy time.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- The LangGraph Research Agent (research_agent.py) serves as the autonomous
  reasoning core because it can decide its own sequence of tool calls at runtime,
  pivoting when a venue is full or a constraint cannot be satisfied — behaviour
  that cannot be captured in pre-written rules.

- The Rasa Pro CALM Digital Employee (exercise3_rasa/) handles all human-facing
  confirmation conversations because its explicit CALM flows and Python action
  guards make every decision auditable and every business-rule constraint
  (e.g. MAX_DEPOSIT_GBP) provably enforced, which an open-ended LLM loop cannot
  guarantee.

- The shared MCP Venue Server (mcp_venue_server.py) acts as the single source of
  truth for venue data, because exposing tools over a wire protocol lets both
  agents — and any future client — query the same live database without sharing
  code or a common import path, as demonstrated by the status-change experiment
  in this exercise.

- A Planner-Executor split (Week 3, DeepSeek R1 + Llama 70B) decouples high-cost
  reasoning from high-speed execution, because having one capable model write the
  plan and a faster model carry out the steps reduces latency and token cost for
  multi-turn tasks while keeping the full reasoning trace observable.

- A CLAUDE.md memory layer backed by a vector store (Week 4) gives the research
  agent persistent knowledge across sessions, because without it the agent
  re-discovers things it has already learned (e.g. which venues are consistently
  full on weekends), wasting tool calls and producing inconsistent recommendations.

- An observability and safety guardrail layer (Week 5) wraps the entire pipeline
  because production use requires being able to trace exactly which tool was called
  with which arguments, evaluate whether the agent met the original brief, and
  reject outputs that violate safety constraints before they reach Rod or the
  pub manager.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The LangGraph Research Agent handles the research, and the Rasa CALM Digital
Employee takes the call from the pub manager.

The research problem is inherently open-ended: when I ran Query 1, the agent had
to decide on its own to call search_venues first, then chain a second tool call
to get_venue_details for the top result — nobody told it that two steps were
needed. When I then changed The Albanach's status to "full" for the experiment,
the agent automatically returned only The Haymarket Vaults without requiring any
code change on the client side. That kind of runtime pivot — deciding which tool
to call next based on what the previous tool returned — is exactly what the
ReAct loop is built for.

The confirmation call is the opposite problem: every word can create a legal
commitment or cost money, so improvisation is the enemy. The Rasa action server
enforces MAX_DEPOSIT_GBP as a hard Python guard; there is no prompt that could
talk it into skipping that check. Swapping the agents feels wrong in both
directions: giving the CALM agent the research job would break the moment a
venue is unexpectedly full, because there is no flow branch for every
combination of failure modes. Giving the LangGraph agent the confirmation call
would mean relying on a probabilistic model to never exceed a deposit limit —
a guarantee it structurally cannot provide.
"""
