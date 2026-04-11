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
- FILL ME IN
- FILL ME IN
- FILL ME IN
- FILL ME IN
- FILL ME IN
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
FILL ME IN
"""
