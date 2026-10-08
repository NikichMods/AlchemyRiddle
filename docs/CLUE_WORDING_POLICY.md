# Human-readable clue wording — case 13 follow-up

Current full review, 2026-10-08: all 28 condition phrases (four per seven covered
shapes) are user-accepted as wording. This does not certify generator difficulty
or production integration. Explicit authoring offset enables between-case variety;
surface variation never counts as reasoning diversity. See CLUE_TEMPLATE_SHEET.md.

Keeper-aside review: user rejects the general clipped/aphoristic voice, invented
writing props (quill/lids/mortar), ambiguous standalone "лист", forced explanations
and jokes needing translation. Write plausible personal thoughts in ordinary
Russian, with occasional practical/macabre humor and distractions such as lunch
or other Keeper work. No obligatory two-part punchline; not every note must be
about handwriting. A reading must work without staging an unseen writing scene.
Follow-up review accepts the conversational voice and specifically keeper-lunch-v1,
keeper-cemetery-v1, keeper-shovel-v1, keeper-corpses-v1 and keeper-important-v1.
User authorizes rewriting even the six retained old notes, reducing handwriting
dominance, more varied punctuation and more mild black humor (no graphic cruelty).
Punctuation should follow an actual thought/pause, not a new mandatory pattern.
The latest user request rewrites those first five too, in the freer voice of the
remaining nineteen. New lunch/cemetery/shovel/corpses/important-v2 lines replace
their v1 counterparts for future authoring; v1 text remains historical and accepted
as an earlier wording. All 24 current lines are review candidates, not individual
acceptance. Topics remain ordinary Keeper work, cemetery, rest, lunch, curiosity,
commerce and a small writing-related subset. There is no quota of thirty.
Old IDs/text remain valid for historical records, but rejected lines are no longer
eligible for future authoring. No repeated-play/event/answer-dependent flavor.

Current refinement after case 14, 2026-10-08: human wording is required in the
condition itself, not only its aside. Semicolon XOR felt robotic and conflicted
with the human note; target-prohibition wording was praised as natural. New
authoring uses xor-plain-v2: "Выполняется ровно одно из двух условий: либо …,
либо …". Old xor-plain-v1 text is immutable and still validates. Generic future
count fallback also avoids semicolon lists under plain-fallback-v2; old fallback
remains readable. Optional aside pool has thirty lines in keeper-asides.mjs,
without answer dependence, new hints or invented past player events. Small italic
separate presentation is liked; cross-line voice coherence needs further evidence.
No new requirement to lengthen a solved puzzle or increase aside frequency.

2026-10-08. User rejects singleton "exactly zero of these statements" as unnatural.
Direct predicate/negation is the accepted repair. Also requested an explicit
distinction: stable adjacent pairs are necessary, but all target composition
conditions must hold as well. Research UI/text only; production remains BLOCKED.

Implemented: single positive assertion says the named component has the property;
single negative assertion says it does not. Multi-statement zero becomes "none of
the following statements hold". Canonical property spelling/slot names retained.
Evaluator and fixture AST unchanged. A completed trial's original public wording
snapshot remains frozen; corrected rendering must not rewrite its recorded play.

## Controlled variation in future research cases

User suggests calm natural wording and potentially immersive variants, with exact
logic preserved. The bounded Lab authoring layer uses small reviewed templates
per predicate/operator, selected deterministically at authoring time. A full
production phrase generator is not implemented or accepted as a production seam.
Persist template identity and exact text with the immutable case. No free-form runtime
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

Completed bounded artifact: [CLUE_TEMPLATE_SHEET.md](CLUE_TEMPLATE_SHEET.md),
with 28 accepted core phrases, 24 optional Keeper-aside review candidates, applicability
guards and semantic checks. Future Lab integration is implemented through explicit
offline authoring and validated frozen wording records; production integration is
not implemented. No extra blind
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

User review, 2026-10-08: all six plain-language example pairs are accepted as
wording directions. This does not accept a runtime phrase generator. Generic
"Запись алхимика" framing is rejected as insufficiently connected to this game.
Future flavor drafts require identifiable Graveyard Keeper context. They must
not replace properties with imagery, imply chemistry or act as an answer tell.

### Accepted flavor direction and event consistency

User review, 2026-10-08: prefer short notes by the Keeper, occasionally with
character. Plain exact conditions remain primary; restrained personal asides are
accepted as the flavor direction. Template selection is offline, never during play.
Clotho is an appropriate world reference, but "Клото отдельно подчеркнула"
creates dissonance when the player never had that conversation. Do not invent
past conversations, completed quests, experiments or NPC statements as flavor.
Any wording claiming such an event requires established player-state evidence.
Keeper notes may present the supplied constraint without claiming an unperformed
discovery. Asides implying prior mistakes are illustrative, not universal defaults.
NPC delivery/integration remains unselected.

Bounded reference review: Clotho is the game's alchemy introduction; the official
game description emphasizes practical resource use, ethically dubious economy
and macabre humor. This supports proposing Clotho-related notes or the Keeper's
own laboratory notes. It does not establish canonical authorship/dialogue for
new mod clues. No new delivery mechanism or NPC integration is selected.

Sources (accessed 2026-10-08):
- https://graveyardkeeper.fandom.com/ru/wiki/%D0%9A%D0%BB%D0%BE%D1%82%D0%BE
- https://store.steampowered.com/app/599140/Graveyard_Keeper/

Illustrative independent drafts, not a recipe or quotations from the game:
- Reviewed Clotho-associated note (not eligible without a matching real event):
  Клото отдельно подчеркнула: порошок не должен иметь свойства «Трупное».
  Остальное на полях разобрать не удалось.
- Keeper's laboratory note: Порошок без свойства «Трупное». Записать крупнее,
  пока снова не перепутал банки.
- Keeper's laboratory note: Для этой смеси нельзя одновременно взять жидкость
  со свойством «Насекомое» и эссенцию со свойством «Орган». Подчеркнуть дважды.
  В прошлый раз одного подчёркивания оказалось мало.

Flavor must stay separate from the exact assertion. Legibility matters more than
making each condition a joke. Keeper-note style is accepted; individual templates
still need semantic/event-scope review before use. Existing completed cases remain
frozen. The future-case renderer now supports explicit versioned wording plus a
separate optional aside; existing unannotated fixtures use the legacy path.

Presentation boundary: automatic review rejected restarting completed case 13 to
show new wording, citing original player-facing text preservation. No restart
occurred. Corrected clue renderer applies to future cases; original played
snapshot and running case renderer preserved. Source history records the repair.
