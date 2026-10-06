# Prototype 33 — Theoretical reagent to practical source flow

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: precommitted before first player action.

Purpose: validate the end-to-end investigation state machine, not re-test whether
Candidate A tag-constraint puzzles are intrinsically enjoyable.

Branch: `research/prototype-33-theoretical-reagent-flow`
Base main: `e55dab4320c113c8e3cda2f4c8a831afea0da8a4`
Production remains BLOCKED.

## Scenario entry

The journal already contains one visible unknown-product need:
- target: **Сумеречный раствор**
- arity: two-slot (Powder + Liquid)
- status before start: research lead available
- difficulty label shown: **Учебное исследование**
- world-time indicator while research UI is open: **Время остановлено**

The player has sufficient Science for this scenario: **6 Science**.
Starting the deduction itself costs 0 Science.

Only one unsolved deduction may be active. No other deduction is active.

## Candidate field after Start Research

Powders:
- P1 **Серый пепел** — properties: {Минерал}; practical route already known
- P2 **Споровый порошок** — properties: {Растение}; practical route already known

Liquids:
- L1 **Масляная вытяжка** — properties: {Животное, Насекомое}; practical route already known
- L2 **Токсичная жидкость** — properties: {Растение, Насекомое}; **identity/properties known only through this theoretical research; practical source route unknown**

The player is allowed to see the exact real-style identity `Токсичная жидкость`
and its properties despite not having produced it.

## Target constraints

All visible from the start:
1. **Растение встречается ровно в одном из двух компонентов.**
2. **Ровно одно из утверждений верно:**
   - порошок имеет признак `Минерал`;
   - жидкость имеет признак `Животное`.
3. **Если жидкость имеет признак `Насекомое`, порошок имеет признак `Минерал`.**

Literal semantics. No hidden properties/exceptions.

## Hidden answer

**P1 Серый пепел + L2 Токсичная жидкость**.

Constraint check:
- P1+L1: Plant count 0 -> fails #1.
- P1+L2: Plant count 1; XOR Mineral=true/Animal=false; Insect liquid -> Mineral powder -> passes all.
- P2+L1: Plant count 1; XOR Mineral=false/Animal=true; Insect liquid -> powder must Mineral -> fails #3.
- P2+L2: Plant count 2 -> fails #1; also #2 false/false and #3 fails.

Thus unique.

## Deduction resolution semantics

When the player independently derives P1+L2:
- mark deduction complete;
- advance two-slot difficulty progression by one completed investigation;
- free the one-active-deduction slot;
- record formula as known recipe knowledge immediately;
- in the simulated cauldron known-recipe list show:
  `Сумеречный раствор — Серый пепел + Токсичная жидкость`;
- do NOT grant possession or practical source/decomposition knowledge for L2.

Journal state after deduction:
- target: `Формула выведена`;
- practical blocker: `Токсичная жидкость — способ получения неизвестен`;
- other new target deductions could now be started, but this prototype remains
  focused on finishing the practical flow.

## Source-research action

Available journal action on L2:
- **Исследовать способ получения**
- cost: **2 Science** (prototype interaction cost, not accepted balance)
- deterministic result:
  - source material: **Красный гриб**
  - preparation: **перегонка в алхимическом кубе**
  - practical unlock requirement remains: find and Study the source material
    through the normal vanilla research process before the decomposition route
    can be used.

After action:
- Science: 4;
- journal records exact source/preparation route;
- no physical item is granted;
- no vanilla Study/decomposition unlock is granted by the source-research action;
- practical next task: obtain Красный гриб -> Study it -> process it -> obtain
  Токсичная жидкость -> synthesize known Сумеречный раствор formula.

## Final state for paper prototype

The prototype stops after source/preparation research is revealed. It does not
simulate ordinary gathering/Study/crafting actions, because their purpose in
this test is only to establish that the flow hands cleanly back to vanilla play.

## Leave/resume semantics

At any point while deduction is active:
- player may exit research UI;
- world time resumes;
- returning shows `Продолжить исследование` and restores exact field/clues/marks;
- other target leads remain visible but cannot start until deduction completes.

After deduction completes:
- no deduction lock remains;
- solved formula/source tasks remain journal entries and can be resumed later.

## Evaluation questions

Observe:
- does seeing exact L2 name/properties before physical discovery feel acceptable;
- does unique deduction still feel complete even though one ingredient is
  practically unavailable;
- does immediate appearance in known-recipe list feel earned/natural;
- is `formula known but ingredient source unknown` legible rather than confusing;
- does the separate 2-Science source research feel like coherent goal-first
  investigation or like an embedded wiki button;
- does handing back to normal Study/acquisition feel satisfying or redundant;
- does the sequence feel too layered/bureaucratic.

Do not change any rule/result after play starts.


## Live checkpoint 1

Player UX feedback:
- the heading that says the target research 'gave' the clue set is misleading because no prior research action occurred; use neutral wording such as known target facts/observations rather than inventing an extra progress-bar action;
- the explicit wording 'exactly one' was clear;
- this 2x2 puzzle felt too complex for a tutorial because two of three clues are compound; provisional difficulty feels closer to medium;
- field size, clue count/complexity, and later relation density should all contribute to difficulty.

Player independently deduced the unique pair P1 + L2. This matches the precommitted answer.

The player proposed a possible paid 'check combination' action. It is not added mid-prototype. Under the precommitted rules, unique deduction itself completes this investigation without spending Science.

Transition:
- deduction complete;
- two-slot progression advances one step;
- active deduction slot freed;
- Science remains 6;
- the formula is now known in the simulated recipe list;
- L2 remains practically unmastered and its source is still unknown;
- next available action: research the source of L2 for 2 Science.


## Live checkpoint 2 — confirmation-cost clarification and source research action

Player clarified that a paid formula-confirmation action is not ceremonial if the player may submit any candidate pair and receive success/failure feedback. A free success/failure oracle would permit brute-force clicking without reasoning.

Design conclusion for future prototypes/production candidate:
- formula submission / hypothesis confirmation should consume a non-zero research resource when it can be invoked on arbitrary candidate formulas;
- Science is the leading resource;
- prototype working value suggested by player: 1 Science per submitted formula;
- exact cost and wrong-answer feedback semantics remain open;
- do not retroactively alter Prototype 33's precommitted economy. In this run Science remained 6 after deduction.

Player also specified the desired success transition:
- explicit success acknowledgement;
- show the now-known formula and its components;
- compare component mastery/practical availability;
- if any component is not practically mastered, surface a clear message such as `Доступно исследование способа получения: <reagent>`;
- add the corresponding source-research action to the journal;
- after theoretical solve, the player is free to start a new deduction or pursue reagent-source research.

Player now chooses the precommitted action:
- `Исследовать способ получения Токсичной жидкости`
- cost: 2 Science.

Deterministic result from precommit:
- source material: Красный гриб;
- preparation: перегонка в алхимическом кубе;
- practical requirement remains: obtain and Study the source through normal vanilla research before the decomposition/preparation route can be used.

State after source research:
- Science: 4;
- formula remains known;
- source/preparation knowledge for Токсичная жидкость is now known;
- no physical item granted;
- no vanilla Study/decomposition completion granted;
- next ordinary-world task: obtain Красный гриб -> Study -> process -> obtain Токсичная жидкость -> synthesize the known target formula.


## Final player evaluation

The end-to-end flow is accepted experientially.

Player judgement:
- the sequence feels natural:
  `deduce formula -> identify missing practical reagent knowledge -> research source -> return to ordinary play`;
- compared with vanilla, the flow is dramatically clearer and more actionable;
- no obvious conceptual contradiction, confusion or immersion break was found;
- the added structure does not feel like arbitrary mod configuration; it feels
  like making previously implicit alchemical knowledge/progress explicit.

Important journal/compendium refinement:
- do **not** rely on transient research-history messages to preserve source
  knowledge;
- do **not** need a verbose status such as "practical mastery still ahead";
- once a source/preparation route has been researched, that result should become
  durable reference data;
- maintain a unified reagent compendium/database for **all known reagent
  identities**, not only reagents that happened to be missing during one target;
- for each known reagent, show whether a source/preparation route is known;
- when known, show the durable route;
- when unknown, expose the source-research action where appropriate.

This makes paid source research persistent player knowledge rather than a log
entry the player must later rediscover.

Prototype disposition:
**PASS. RETAIN THEORETICAL-REAGENT -> SOURCE-RESEARCH FLOW.**

The prototype does not validate final UI layout, wording, exact Science costs,
or runtime/save implementation ownership.

Production remains BLOCKED.
