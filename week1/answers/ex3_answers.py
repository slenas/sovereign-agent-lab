"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £200 deposit
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £500 deposit
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "ActionValidateBooking class has a run method that has a number of guardrails with certain designated actions if any of them is violated. There's a clear guardrail on any deposits above £300. Since the model interpreted the proposed deposit correctly at £500 this exceeds that £300 guard value so the agent escalates."   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160
And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
CALM managed to identify that the question was out-of-scope, and router the flow towards the out-of-scope handler. As a direct result of that, it informed the user that it's not trained to help with that and rightly asked the user to contact the organiser directly.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
Both approaches worked as expected. Using LangGraph, the agent was able to detect the out of scope question and suggest an alternative. CAML performed in a similar way, clearly stating that cannot help with that request but its response was more chatbot oriented and guided rather than human-like.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I run the above dialog after 16:45. The system detected the now() UTC time and based on that it needed to escalate the request as we just activated in actions.py another guardrail around the time the request is made.
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160
And how many of those guests will need vegan meals?
Your input ->  50
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  200
I need to check one thing with the organiser before I can confirm. The issue is: it is past 16:45 — insufficient time to process the confirmation before the 5 PM deadline. Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
CALM shifts a lot of responsibility from hand-written deterministic code to the LLM: intent recognition, mapping messy phrasing to structured slots, and deciding when a flow should fire. In old Rasa, it encoded that behavior explicitly with NLU examples, rules, and regex-heavy validation code; now it describes it and let the model infer.
Python still owns what should never be “best guess”: business rules, thresholds, and guardrails (e.g., what counts as valid confidence, when to reject, when to escalate). That boundary is important: language interpretation can be probabilistic, but policy should remain deterministic and auditable.
What I trusted more in the old approach was reproducibility. If an utterance matched a rule yesterday, it would match tomorrow. CALM gains speed of development and better handling of natural language variation, but it introduces model variability and prompt/flow sensitivity. So the trade-off is clear: much less plumbing and better UX coverage, in exchange for less transparent failure modes and a stronger need for robust validation, observability, and fallback design.

Think about:
- What does the LLM handle now that Python handled before?
- What does Python STILL handle, and why (hint: business rules)?
- Is there anything you trusted more in the old approach?
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
The CALM setup cost buys a controlled conversational product surface, not open-ended agency. With config/domain/flows/actions wired correctly, you get predictable task completion, explicit handoff paths, and cleaner governance over what the bot is allowed to do. That is valuable in production support settings where consistency and safety beat creativity.
Compared with LangGraph, CALM cannot freely improvise arbitrary multi-step reasoning or dynamically call tools that were never declared in `flows.yml` and the domain/action layer. Its behavior is intentionally constrained by designed flows and available actions. For confirmation workflows, that constraint is mostly a feature: users need accuracy, compliance, and stable outcomes more than novelty.
The limitation appears when requests drift outside predefined capabilities. LangGraph can often compose a new plan on the fly; CALM will usually redirect, fallback, or fail gracefully. So the setup overhead buys reliability and control, while sacrificing general-purpose flexibility and spontaneous tool orchestration.


Be specific. What can the Rasa CALM agent NOT do that LangGraph could?
Is that a feature or a limitation for the confirmation use case?
Think about: can the CALM agent improvise a response it wasn't trained on?
Can it call a tool that wasn't defined in flows.yml?
"""
