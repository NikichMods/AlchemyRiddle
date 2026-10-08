# Human-readable clue wording — case 13 follow-up

2026-10-08. User rejects singleton "exactly zero of these statements" as unnatural.
Direct predicate/negation is the accepted repair. Also requested an explicit
distinction: stable adjacent pairs are necessary, but all target composition
conditions must hold as well. Research UI/text only; production remains BLOCKED.

Implemented: single positive assertion says the named component has the property;
single negative assertion says it does not. Multi-statement zero becomes "none of
the following statements hold". Canonical property spelling/slot names retained.
Evaluator and fixture AST unchanged. A completed trial's original public wording
snapshot remains frozen; corrected rendering must not rewrite its recorded play.

## Proposed controlled variation

User suggests calm natural wording and potentially immersive variants, with exact
logic preserved. Retain as a design direction; a full phrase generator is not yet
implemented or accepted as a production seam. Recommended mechanism: small
reviewed templates per predicate/operator, selected deterministically at authoring
time. Persist template identity with the immutable case. No free-form runtime
language generation or unrecorded paraphrasing during play.

| Meaning | Base wording | Precision boundary |
| --- | --- | --- |
| Slot has property | Порошок имеет свойство «А». | Only the named slot |
| Slot lacks property | Порошок не имеет свойства «А». | Negation of that exact property |
| XOR | Выполняется ровно одно из двух условий: … | Exactly one, not inclusive either |
| Implication | Если выбран порошок со свойством «А», эссенция должна иметь свойство «Б». | No claim converse or that А must hold |
| Target-specific forbidden combination | Для этой смеси нельзя одновременно взять жидкость со свойством «А» и эссенцию со свойством «Б». | Not a chemical pair-incompatibility result |
| Count | Среди компонентов ровно два имеют свойство «А». | Remaining components lack А |

Flavor framing may decorate these assertions but must not imply reagent origin,
extra property, chemical compatibility or author intent. Synonym variation does
not count as reasoning diversity. Surface wording and effective logical work are
separate review axes; simplify under actual field constants before labeling depth.

Next artifact recommendation: a small phrase sheet with base/alternative templates
and predicate equivalence examples, reviewed before integration. No extra blind
case, automatic clue checking or partial failure explanation introduced here.

## Concrete draft variants for review

These examples are not a runtime selection algorithm. Canonical property names
stay unchanged in quotes/badges; each alternate retains exact predicate meaning.

- Negative literal: Порошок не имеет свойства «А» / Для этого состава нужен
  порошок без свойства «А».
- Positive literal: Эссенция имеет свойство «Б» / У выбранной эссенции должно
  быть свойство «Б».
- XOR: Выполняется ровно одно из двух условий: … / Должно выполняться одно
  из этих двух условий, но не оба: …
- Implication: Если порошок имеет свойство «А», эссенция должна иметь свойство
  «Б» / При выборе порошка со свойством «А» нужна эссенция со свойством «Б».
- Target prohibition: Для этой смеси нельзя одновременно взять жидкость со
  свойством «А» и эссенцию со свойством «Б» / В этом составе такое сочетание
  жидкости со свойством «А» и эссенции со свойством «Б» не допускается.
- Count: Среди трёх компонентов ровно два имеют свойство «А» / Свойство «А»
  должно быть у двух выбранных компонентов, а у третьего его быть не должно.

Immersive framing such as В заметке о составе указано: … can prefix a precise
assertion. It must not replace properties with imagery or imply chemistry.
Phrase choice must not act as a hidden answer tell.

Presentation boundary: automatic review rejected restarting completed case 13 to
show new wording, citing original player-facing text preservation. No restart
occurred. Corrected clue renderer applies to future cases; original played
snapshot and running case renderer preserved. Source history records the repair.
