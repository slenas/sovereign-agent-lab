"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
We see that the model is able to correctly answer the question in all three input modalities. 
This is expected because the question is straightforward, the model we're using is big enough (70B parameters) to support way much more complex scenarions.
As the assignment suggested, The Albanach appears in both teh XML and Sandwich input modalities, suggesting that the model returned the entry matched the criteria first.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The Holyrood Arms is the more dangerous distractor.
It matches 2 out of 3 required constraints (capacity=160, vegan=yes).
It only fails on status=full, which is easy for a model to miss if it’s scanning quickly and in terms of context it doesn't have necessarily a negative connotation.
It sits immediately before the true target (The Haymarket Vaults), so the entries are highly confusable in local context.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
What's strange here is that the model is able to correctly answer the question in all three input modalities.
What's even stranger is that the model returned the same answer in all three input modalities which was also the "optimal" one as it was matching closer all the criteria.
Maybe if an even weaker model was used, the model would have missed the answer in at least one of the three input modalities.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Even small models can be able to answer the question correctly if the question is straightforward and the provided input is small.
What that means is that the attention mechanism is able to focus on the correct answer and doesn't just skim through the input.
"""
