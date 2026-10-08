# Deduction and experimental onboarding — bounded comparison

2026-10-08. Design/research; no production implementation or changed logic.

## Question and evidence

After case 18, the user requests a comparison with actual games and combines
conditional-clue concerns with an explicit tutorial requirement. The playtester's
overall impression is reported as predominantly positive. The case did not feel
like a boss, only-with wording invited a mandatory-conjunction reading, a fourth
condition felt unused, and empty prior knowledge felt unlike late progression.
The exact audit and immutable outcome remain in the case-18 checkpoint.

Question: should all clues be active in the final answer, or should the game
explicitly teach deduction interleaved with experiments? These are different
issues: every clue must hold, but each individual solve need not explicitly derive
something from every clue. A rule can reject an alternative without its antecedent
being true in the final answer. Tutorials must not license ignoring constraints.

## Primary game examples

- [Clues by Sam official tutorial](https://cluesbysam.com/s/tutorial/): promises
  a provable next identification and disallows guesses. Clarifies conditional
  direction and contraposition explicitly. Allows dimming clues no longer useful
  and lightly highlights referenced identities. Demonstrates explicit expectations
  and terminology, not a requirement for every conditional antecedent to hold.
- [Alchemists official interactive rules](https://alchemists.czechgames.com/rules/):
  begins with a guided experiment, explains how its outcome excludes possibilities,
  teaches an unexciting neutral result as informative, then invites further
  experiments. Closest comparator for teaching an experiment/deduction cycle;
  its chemistry and multiplayer economy are different from this project.
- [Chants of Sennaar designer interview](https://www.gamedeveloper.com/design/immersing-players-in-the-culture-of-a-people-with-language-puzzler-chants-of-sennaar):
  designer Julien Moya describes revisable hypotheses, repeated observations in
  different contexts, early guidance and consistent visual rules. Supports
  repeated opportunities to understand/check a rule, not one explanation alone.
- [Golden Idol designer interview](https://www.gamedeveloper.com/design/case-of-the-golden-idol):
  Andrejs Klavins describes frustration with undifferentiated whole-case failure,
  intermediate progress, multiple paths to a conclusion and reducing information
  load. Useful analogy for feedback and nonidentical solve paths; not authorization
  to import partial-answer disclosure or red herrings into our clue contract.

These are read rule/tutorial pages and developer accounts, not direct fresh
playthroughs, population evidence or a universal genre consensus. No story or
recipe solutions were needed. Experimental deduction is compatible with logic;
it differs in when the player obtains facts, not whether facts remain binding.

## Accepted tutorial direction and proposed execution

User explicitly requires clear, visible teaching in the existing introductory
investigations. A small easy puzzle alone is insufficient. Separately teach the
new three-slot pair-compatibility layer. Presentation format (popup, contextual
panel or another form) and exact wording remain unaccepted implementation choices.

Proposed teaching sequence, not a newly accepted ladder or generator gate:
1. Under two-slot low load, show where powder/fluid roles and properties are read,
   that all conditions constrain one mixture, and how to submit a hypothesis.
2. At first three-slot research, demonstrate the two adjacent pair experiments,
   their binary result, journal, cost and relationship to whole-mixture checks.
   Show an incompatible result as useful exclusion, not failed play.
3. Demonstrate that a stable chain can still violate a composition condition,
   and that if A then B does not require choosing A. Use fictional teaching data;
   require player action/understanding without revealing an unknown real recipe.
4. End guidance, retain a compact reopenable reference, and verify independent
   transfer to a fresh ordinary puzzle. Do not require analysis feedback during
   the user's current example-only phase unless they initiate it.

Tutorial success should be comprehension/transfer: player distinguishes roles,
knows legal pair types, understands what observations establish, and can choose
a justified investigation without facilitator explanation. A solved teaching
example alone is insufficient, as case 18's stronger accidental reading succeeded.

## Consequences and unresolved decisions

Retain formal clue necessity and semantic precision; do not add padding clues or
force all conditional antecedents true. Such a gate changes solution sets and
can flatten branch reasoning into direct requirements. Undesirable obligation-like
wording needs a separate versioned repair; old cases remain immutable.
Tutorials do not compensate for genuinely irrelevant clues or unsupported boss
claims. Future boss candidates need an actual multi-stage public reasoning route
under plausible frozen player knowledge. No arbitrary guaranteed initial pair
count is accepted; do not hide accumulated correct knowledge to manufacture work.
Next step proposed: prepare the first compact guided teaching scenario for review,
then test independent understanding; not another nominal boss obtained by adding
cards and conditions. No tutorial UI or generator weights changed in this review.
