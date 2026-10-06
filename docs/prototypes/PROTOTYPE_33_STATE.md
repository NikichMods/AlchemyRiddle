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
