# Keeper contextual reactions — approved editorial bank

Status: 2026-10-08, **research-only**. User-approved exact wording from
the separate editorial review. Not a production mod feature.

## Authoring and historical integrity

- **13 clue asides** are active for **new** Puzzle Lab authoring in
  `research/PuzzleLab/keeper-asides.mjs` (`authoringAsides`).
  `clueAsideFits(f,clue,id)` requires the specified, visible logical structure,
  named slots and tag names before attaching an aside. The `--aside` workflow
  remains explicit, optional, and limited to one aside per investigation.
- **9 event reactions** are stored in `eventAsides` with their proposed event
  and matching context. **They are editorially accepted but not yet displayed** by
  the Puzzle Lab event UI; there is no automatic selection, per-run frequency
  or seen-history behavior in the current code.
- Old IDs and exact text remain in `asides` for frozen historical records,
  but are not in the future-case pool. Never rewrite played cases.
- Text is never generated or freely paraphrased at game runtime. Optional
  future selection should depend only on visible clue structure/tags or a
  result the player has just learned; no answer leakage or new mechanical hint.
- The fixed clue remains authoritative; artistic text is secondary. Do not
  show an aside automatically after every action. Repetition control and
  any additional UI placement require separate implementation/verification.
- Tag jokes use **associations**, not claims that a given property establishes
  a particular physical ingredient or a hidden compatibility rule.

## Active context-specific clue asides (13)

| ID | Trigger: visible condition | Approved aside |
| --- | --- | --- |
| `clue-xor-insect-slime-v1` | Exactly one: powder Насекомое / fluid Слизь | Хорошо, что выбирать можно глазами. На ощупь — увольте. |
| `clue-count-corpse-v1` | Exactly two of three tags Трупное | Два с „Трупным“? Ну, это по моей части. |
| `clue-has-organ-v1` | Essence has Орган | „Орган“... Церковный или из морга? |
| `clue-lacks-slime-v1` | Fluid lacks Слизь | Без „Слизи“? Уже звучит гораздо приятнее. |
| `clue-has-dark-v1` | Essence has Тёмное | „Тёмное“? Вот эту страницу инквизитору лучше не показывать. |
| `clue-count-plant-v1` | Exactly two of three tags Растительное | Похоже, я алхимик с уклоном в садоводство. |
| `clue-implies-donkey-v1` | Powder Животное → essence Растительное | Животному подавай растительное. Прямо как ослу морковку. |
| `clue-xor-suspicious-v1` | Exactly one: fluid Тёмное / essence Трупное | Что ни выбери — всё звучит подозрительно. |
| `clue-forbids-slime-corpse-v1` | Cannot combine fluid Слизь and essence Трупное | Да я, собственно, и не настаивал. |
| `clue-lacks-mineral-v1` | Powder lacks Минеральное | Камни мне ещё для надгробий пригодятся. |
| `clue-count-slime-v1` | Exactly two of three tags Слизь | Два со „Слизью“? Пожалуй, крышки стоит закрыть поплотнее. |
| `clue-shared-jerry-v1` | All three selected slots share a tag | Общее у троих... Джерри бы начал с выпивки. |
| `clue-has-insect-v1` | Essence has Насекомое | „Насекомое“? Лишь бы из банки никто не выполз. |

All tags above are exact canonical labels, not informal inferred synonyms.
The order of two symmetric XOR/prohibition terms may vary without changing the
meaning; implication direction must remain exact.

## Approved event reactions, not yet wired to UI (9)

| ID | Event and required visible context | Approved reaction |
| --- | --- | --- |
| `pair-stable-insect-slime-v1` | Newly tested stable pair, tags Насекомое + Слизь | А ведь поладили. Та ещё парочка. |
| `pair-unstable-insect-slime-v1` | Newly tested unstable pair, tags Насекомое + Слизь | Не сошлись. Да и компания, прямо скажем, на любителя. |
| `submit-failed-curiosity-v1` | Failed complete-mixture submission | Не то. Интересно, что я упустил? |
| `submit-success-beauty-v1` | Successful complete-mixture submission | Вот теперь всё сошлось. Красота. |
| `pair-unstable-plant-corpse-v1` | Unstable pair, tags Растительное + Трупное | Не срослось. Бывает даже с растениями. |
| `pair-unstable-discovery-v1` | First observation of a previously untested unstable pair | Не подошли? Отлично, эту пару можно вычеркнуть. |
| `pair-unstable-mineral-slime-v1` | Unstable pair, tags Минеральное + Слизь | Не склеились. А я-то на слизь рассчитывал. |
| `pair-stable-insect-corpse-v1` | Stable pair, tags Насекомое + Трупное | Сошлись. В морге такое соседство не удивило бы. |
| `submit-success-after-failure-v1` | Successful formula, after an earlier failed full submission | Вот оно! Хорошо, что первой догадкой я не ограничился. |

The two tag requirements for a pair refer only to the *selected tested pair*;
they do not assert that a particular tag caused the measured result.
Event reactions must only be shown after the outcome is revealed.

## Earlier 16 voice references — not active beneath individual conditions

The following earlier lines were liked as conversational-voice examples, but
were **not reviewed/approved for placement under particular logical clues**.
They remain editorial references for potential future overall-investigation
or journal placements, not active authoring options:

1. Когда вернусь домой, попробую рассказать про алхимию. Про остальное, пожалуй, промолчу.
2. Наверху церковь, внизу алхимия. Хорошо хоть между работами далеко ходить не надо.
3. У меня есть говорящий череп. И почему-то формулу всё равно приходится разгадывать самому.
4. Сначала понять, потом смешивать. Приятно хотя бы иногда заниматься делом в таком порядке.
5. С этой смесью хотя бы ясно, чего я не знаю. С остальными делами так не всегда.
6. Интересно, епископ назвал бы это чудом или дополнительной работой?
7. Запишу. Через неделю мне самому понадобится объяснение.
8. Разбираюсь уже не только потому, что нужно. Кажется, мне и правда интересно.
9. К моргу я уже привык. А вот к тому, что я теперь ещё и алхимик, — не совсем.
10. Надо бы поесть. Но ведь за едой я всё равно буду думать об этой формуле.
11. С порошками удобно: им всё равно, какой сегодня день недели. С местными жителями так не выходит.
12. Если ничего не получится, хотя бы не придётся никого хоронить. Уже плюс.
13. Вот бы придумать что-нибудь, что само приносит монеты. Я бы с удовольствием занялся такой алхимией.
14. Джерри наверняка нашёл бы, что посоветовать. И что выпить за мой счёт.
15. Надо же, мне уже мало знать, что с чем смешивать. Хочется понять, почему это работает.
16. Иногда мне кажется, что однажды я вернусь домой и буду скучать по этой работе. Иногда.

These were **not** the current set of 22 context/event-approved lines.
The editorial evolution toward short, attached contextual reactions supersedes
using these freely under individual logical predicates.

## Unaccepted / deferred examples

- «Ага. Даже между камнями что-то растёт.» — indirect multi-hop tag analogy;
  **reserve, not active**.
- «Растительное или животное? Прямо контрольная по биологии.» — **reserve**,
  considered adequate but not fully accepted.
- «С растительным — сразу слизь? Прямо как после слизней на грядках.» —
  **rejected**, forced association.
- «Пары поладили. Теперь бы мне поладить с условиями.» — **not accepted**:
  can misdescribe the source of a failed full submission; do not enable.

## Unique-solution invariant (existing)

`rules.mjs`: `validFormula(f, tuple)` requires all clue predicates and all
applicable stable adjacent pairs. `validate(f)` accepts a fixture only if
exactly **one** such tuple exists and equals `f.answer`. A fully valid tuple
cannot be deliberately rejected in a *validated* case as some different secret
answer. No new one-solution rule is needed. Separate product quality evidence
must still establish that players can infer the unique answer from accessible
observations within acceptable effort.

Reference: `docs/CLUE_WORDING_POLICY.md` and
`docs/CLUE_TEMPLATE_SHEET.md`. Production implementation remains BLOCKED.
