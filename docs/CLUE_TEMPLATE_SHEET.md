# Keeper-note templates — bounded wording review

2026-10-08. Design/research artifact; implemented in future-case Lab authoring,
not a production mod change.
The six plain-language directions and occasional Keeper-note character are user
accepted. This sheet instantiates that direction with stable template identities;
it does not claim that every new line received individual player acceptance.
No completed case is rewritten. No real recipe or ingredient identity is present.

## Template set

Placeholders denote the selected component in the named slot, never every card
available in that slot. Preserve exact canonical property names in quotes.
The examples below are independent, not a combined recipe.

| ID | Scope | Russian text |
| --- | --- | --- |
| has-plain-v1 | One positive literal | Эссенция имеет свойство «А». |
| has-note-v1 | One positive literal | У эссенции в этой смеси должно быть свойство «А». |
| lacks-plain-v1 | One negative literal | Порошок не имеет свойства «А». |
| lacks-note-v1 | One negative literal | Для этой смеси нужен порошок без свойства «А». |
| xor-plain-v1 | Exactly one of two assertions | Выполняется ровно одно из двух условий: порошок имеет свойство «А»; эссенция имеет свойство «Б». |
| xor-note-v1 | Exactly one of two assertions | В этой смеси либо порошок имеет свойство «А», либо эссенция имеет свойство «Б» — но не оба одновременно. |
| implies-plain-v1 | A implies B | Если порошок имеет свойство «А», эссенция должна иметь свойство «Б». |
| implies-note-v1 | A implies B | При выборе порошка со свойством «А» нужна эссенция со свойством «Б». |
| forbids-plain-v1 | Not both A and B, target-specific | Для этой смеси нельзя одновременно взять жидкость со свойством «А» и эссенцию со свойством «Б». |
| forbids-note-v1 | Not both A and B, target-specific | В этом составе сочетание жидкости со свойством «А» и эссенции со свойством «Б» не допускается. |
| count-two-plain-v1 | Three selected slots, same property, count 2 | Среди трёх выбранных компонентов ровно два имеют свойство «А». |
| count-two-note-v1 | Three selected slots, same property, count 2 | Свойство «А» должно быть у двух выбранных компонентов, а у третьего его быть не должно. |
| shared-plain-v1 | SharedTag, all selected slots | У всех выбранных компонентов есть хотя бы одно общее свойство. |
| shared-note-v1 | SharedTag, all selected slots | Нужно хотя бы одно свойство, которое есть у каждого выбранного компонента. |

SharedTag is included because the existing Lab supports it. Its two new phrasings
remain drafts; they do not add a new logical family. The shared property need not
be the only common property or be named in advance.

Count-two templates require exactly three distinct slot terms for the same tag.
For two-slot puzzles, counts other than two, partial-slot counts or mixed-property
assertions, these templates are ineligible. Preserve exact scope in a plain count
fallback. Zero assertions use explicit negations; a single assertion uses a
positive/negative literal. Do not manufacture variety by hiding a boundary case.

## Optional independent Keeper asides

| ID | Russian text |
| --- | --- |
| note-label-v1 | Записать крупнее, чтобы не перепутать банки. |
| note-underline-v1 | Подчеркнуть. Лучше дважды. |
| note-legible-v1 | Оставить место между строками. Это ещё придётся перечитывать. |

These are intentions, not assertions that the player previously made mistakes,
performed experiments, met NPCs or completed quests. Do not claim new chemical
outcomes, extra restrictions, danger, ingredient origin or recipe purpose.
The aside stays visually separate from the exact condition. Plain conditions are
the default style; use an occasional aside, not a compulsory joke on every clue.
Research authoring defaults to no aside; one can be explicitly attached. This
does not fix production frequency or a stochastic selection algorithm.
Template/aside choice must not depend on which answer, branch or reagent is true.

Example, independent of any live case:

> Для этой смеси нужен порошок без свойства «Трупное».
>
> Записать крупнее, чтобы не перепутать банки.

## Semantic review

For two Boolean assertions A and B, the admitted assignments in order
00 / 01 / 10 / 11 are:

| Family | Admitted assignments | Guard against misreading |
| --- | --- | --- |
| XOR | false / true / true / false | At least one AND not both; neither is invalid |
| Implication A -> B | true / true / false / true | Absence of A does not require absence of B; B does not require A |
| Target prohibition | true / true / true / false | Neither may be chosen; no chemical incompatibility claim |

Positive and negative literal templates admit A=1 and A=0 respectively.
Count-two admits only 011, 101, 110 for three slot assertions. SharedTag admits a
tuple only when the intersection of all selected tag sets is nonempty; pairwise
overlap alone does not suffice for three slots.

The literal phrases, mandatory/exclusive XOR wording, conditional-only implication,
target-scoped prohibition and exact count preserve these admission sets under
ordinary literal Russian reading. Automated enumeration checks the intended
predicates against the existing Lab evaluator; it cannot prove how players read
natural language. Individual wording comprehension remains player evidence.

## Completed check and next boundary

Bounded offline check: 32 Boolean/tag-set cases compared independent predicate
definitions with existing `satisfies`: two positive, two negative, four XOR,
four implication, four prohibition, eight count-two, eight shared intersections.
An additional three-slot pairwise-only overlap counterexample is rejected by both
definitions. No game corpus or answer data used; no renderer/evaluator changed.

Future-case research integration completed: `wording.mjs`, `author-wording.mjs`,
validated persisted IDs and exact text, separate aside rendering. Slot forms cover
Порошок/Жидкость/Эссенция including reversed implications and case endings.
Unsupported shapes/names retain plain fallback. No completed fixture was edited
or restarted. Six additional tests cover template grammar, scope/fallbacks,
answer independence/outcome preservation, corrupted records, exclusive file writes
and HTTP persistence across restart. Complete Lab suite: 33 passing tests.
Next evidence is human readability in a separately precommitted future trial;
no new trial is opened by this integration. Production remains BLOCKED.
