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
| has-choice-v1 | One positive literal | Для этой смеси нужна эссенция со свойством «А». |
| has-scope-v1 | One positive literal | В состав должна входить эссенция со свойством «А». |
| lacks-plain-v1 | One negative literal | Порошок не имеет свойства «А». |
| lacks-note-v1 | One negative literal | Для этой смеси нужен порошок без свойства «А». |
| lacks-choice-v1 | One negative literal | Для этого состава выбирайте порошок без свойства «А». |
| lacks-scope-v1 | One negative literal | В этой смеси у порошка не должно быть свойства «А». |
| xor-plain-v2 | Exactly one of two assertions | Выполняется ровно одно из двух условий: либо порошок имеет свойство «А», либо эссенция имеет свойство «Б». |
| xor-note-v1 | Exactly one of two assertions | В этой смеси либо порошок имеет свойство «А», либо эссенция имеет свойство «Б» — но не оба условия одновременно. |
| xor-either-v1 | Exactly one of two assertions | Для этой смеси нужно одно из двух: порошок имеет свойство «А» или эссенция имеет свойство «Б». Одновременно оба условия выполняться не должны. |
| xor-one-v1 | Exactly one of two assertions | Из этих двух условий должно выполняться только одно: порошок имеет свойство «А» или эссенция имеет свойство «Б». |
| implies-plain-v1 | A implies B | Если порошок имеет свойство «А», эссенция должна иметь свойство «Б». |
| implies-note-v1 | A implies B | При выборе порошка со свойством «А» нужна эссенция со свойством «Б». |
| implies-choice-v1 | A implies B | Для этой смеси порошок со свойством «А» можно взять только с эссенцией со свойством «Б». |
| implies-scope-v1 | A implies B | Если в смеси используется порошок со свойством «А», у эссенции должно быть свойство «Б». |
| forbids-plain-v1 | Not both A and B, target-specific | Для этой смеси нельзя одновременно взять жидкость со свойством «А» и эссенцию со свойством «Б». |
| forbids-note-v1 | Not both A and B, target-specific | В этом составе сочетание жидкости со свойством «А» и эссенции со свойством «Б» не допускается. |
| forbids-choice-v1 | Not both A and B, target-specific | Если для этой смеси берёте жидкость со свойством «А», выбирайте эссенцию без свойства «Б». |
| forbids-scope-v1 | Not both A and B, target-specific | В этой смеси жидкость со свойством «А» и эссенция со свойством «Б» не должны встречаться вместе. |
| count-two-plain-v1 | Three selected slots, same property, count 2 | Среди трёх выбранных компонентов ровно два имеют свойство «А». |
| count-two-note-v1 | Three selected slots, same property, count 2 | Свойство «А» должно быть у двух выбранных компонентов, а у третьего его быть не должно. |
| count-two-choice-v1 | Three selected slots, same property, count 2 | Два выбранных компонента должны иметь свойство «А», а один — не иметь его. |
| count-two-scope-v1 | Three selected slots, same property, count 2 | В этой тройке свойство «А» есть ровно у двух компонентов. |
| shared-plain-v1 | SharedTag, all selected slots | У всех выбранных компонентов есть хотя бы одно общее свойство. |
| shared-note-v1 | SharedTag, all selected slots | Нужно хотя бы одно свойство, которое есть у каждого выбранного компонента. |
| shared-choice-v1 | SharedTag, all selected slots | Все выбранные компоненты должны иметь хотя бы одно общее свойство. |
| shared-scope-v1 | SharedTag, all selected slots | Среди свойств выбранных компонентов хотя бы одно должно встречаться у каждого из них. |

SharedTag is included because the existing Lab supports it. Its four phrasings
remain drafts; they do not add a new logical family. The shared property need not
be the only common property or be named in advance.

Count-two templates require exactly three distinct slot terms for the same tag.
For two-slot puzzles, counts other than two, partial-slot counts or mixed-property
assertions, these templates are ineligible. Preserve exact scope in a plain count
fallback. Zero assertions use explicit negations; a single assertion uses a
positive/negative literal. Do not manufacture variety by hiding a boundary case.

## Optional independent Keeper asides

Current authoring pool: thirty timeless notes. Historical note-tomorrow-v1,
note-legible-v1 and note-drying-v1 remain in the immutable registry only for old
fixtures. New replacements do not promise tomorrow, later or another reading.
Case-15 feedback rejects that temporal mismatch with a perceived one-off puzzle.

| ID | Russian text |
| --- | --- |
| note-label-v1 | Записать крупнее, чтобы не перепутать банки. |
| note-underline-v1 | Подчеркнуть. Лучше дважды. |
| note-quill-v1 | Перо положить подальше от реагентов. |
| note-ink-v1 | Чернила оставить для записей. |
| note-jar-v1 | Подписать банку, а не крышку. |
| note-lid-v1 | Крышки переставляются слишком легко. |
| note-cleanup-v1 | Запись должна пережить уборку. |
| note-mortar-v1 | Не класть этот лист под ступку. |
| note-stains-v1 | Для пятен оставить другой лист. |
| note-margins-v1 | На полях ещё есть место. Пока. |
| note-unhurried-v1 | Почерк разобрать проще, если не спешить. |
| note-abbreviations-v1 | Здесь обойтись без сокращений. |
| note-sermon-v1 | Это заметка, а не проповедь. Покороче. |
| note-scroll-v1 | Свиток красивый. Читаемость полезнее. |
| note-flourish-v1 | Не украшать буквы до неузнаваемости. |
| note-signature-v1 | Внизу оставить место для подписи. |
| note-kindling-v1 | Этот лист хранить с записями, а не с растопкой. |
| note-neatness-v1 | Если получится красиво — хорошо. Если разборчиво — лучше. |
| note-cup-v1 | Убрать от кружки. Бумаге пить не положено. |
| note-working-v1 | Рабочая запись. Парадный почерк необязателен. |
| note-morgue-v1 | Морг отдельно, письменный стол отдельно. |
| note-corpses-v1 | Покойники почерк не оценят. Мне ещё читать. |
| note-trade-v1 | Не отдавать этот лист вместе с товаром. |
| note-margin-scroll-v1 | Пометку на полях не превращать в ещё один свиток. |
| note-draft-v1 | Спрятать от сквозняка. Рабочие записи летать не обязаны. |
| note-lunch-v1 | Не забыть про обед. Эта запись его не заменит. |
| note-grand-v1 | Записать спокойно. В торжественном тоне смесь не нуждается. |
| note-self-legible-v1 | Главное, чтобы это смог прочесть я сам. |
| note-spacing-v1 | Оставить место между строками. Буквам тоже нужен воздух. |
| note-dry-paper-v1 | Бумагу держать сухой. Для жидкости есть банки. |

These are intentions, not assertions that the player previously made mistakes,
performed experiments, met NPCs or completed quests. Do not claim new chemical
outcomes, extra restrictions, danger, ingredient origin or recipe purpose.
The aside stays visually separate from the exact condition. Plain conditions are
the default style; use an occasional aside, not a compulsory joke on every clue.
Research authoring defaults to no aside; one can be explicitly attached. This
does not fix production frequency or a stochastic selection algorithm.
Template/aside choice must not depend on which answer, branch or reagent is true.

Post-case-15 review: twenty-eight active core phrases; four variants for each
of the seven covered families. Twelve added templates preserve existing IDs/text. Explicit authoring variantOffset rotates choice
across cases as well as within a repeated family, independent of hidden truth.
Persist exact chosen IDs/text; no synonym swapping during play. Keep recognisable
anchors (named slots, exact properties, conditional scope and exactly-one).
The added variants are semantically reviewed, not independently player-accepted.

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
and HTTP persistence across restart. Original integration: 33 passing tests. Case-14 refinement: 35 passing tests.
Case 14 was independently solved and liked; its semicolon XOR was rejected.
Future XOR uses xor-plain-v2 with either/or; historical xor-plain-v1 remains valid.
Future fallback uses comma-list count text or explicit zero negations under
plain-fallback-v2; old fallback IDs remain readable. Thirty optional asides now
provide more variety without changing optional frequency or puzzle semantics.
Next evidence is whether human conditions and asides sound like one voice; no
additional trial is opened by this refinement. Production remains BLOCKED.
