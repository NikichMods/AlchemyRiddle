// SPDX-License-Identifier: MPL-2.0
// IDs and text are immutable once used by a frozen case.
export const asides = Object.freeze({
  'note-label-v1':'Записать крупнее, чтобы не перепутать банки.',
  'note-underline-v1':'Подчеркнуть. Лучше дважды.',
  'note-legible-v1':'Оставить место между строками. Это ещё придётся перечитывать.',
  'note-quill-v1':'Перо положить подальше от реагентов.',
  'note-ink-v1':'Чернила оставить для записей.',
  'note-jar-v1':'Подписать банку, а не крышку.',
  'note-lid-v1':'Крышки переставляются слишком легко.',
  'note-cleanup-v1':'Запись должна пережить уборку.',
  'note-mortar-v1':'Не класть этот лист под ступку.',
  'note-stains-v1':'Для пятен оставить другой лист.',
  'note-margins-v1':'На полях ещё есть место. Пока.',
  'note-unhurried-v1':'Почерк разобрать проще, если не спешить.',
  'note-abbreviations-v1':'Здесь обойтись без сокращений.',
  'note-sermon-v1':'Это заметка, а не проповедь. Покороче.',
  'note-scroll-v1':'Свиток красивый. Читаемость полезнее.',
  'note-flourish-v1':'Не украшать буквы до неузнаваемости.',
  'note-signature-v1':'Внизу оставить место для подписи.',
  'note-drying-v1':'Свернуть позже. Чернилам дать высохнуть.',
  'note-kindling-v1':'Этот лист хранить с записями, а не с растопкой.',
  'note-neatness-v1':'Если получится красиво — хорошо. Если разборчиво — лучше.',
  'note-cup-v1':'Убрать от кружки. Бумаге пить не положено.',
  'note-working-v1':'Рабочая запись. Парадный почерк необязателен.',
  'note-morgue-v1':'Морг отдельно, письменный стол отдельно.',
  'note-corpses-v1':'Покойники почерк не оценят. Мне ещё читать.',
  'note-trade-v1':'Не отдавать этот лист вместе с товаром.',
  'note-tomorrow-v1':'Главное, чтобы завтра это смог прочесть я сам.',
  'note-margin-scroll-v1':'Пометку на полях не превращать в ещё один свиток.',
  'note-draft-v1':'Спрятать от сквозняка. Рабочие записи летать не обязаны.',
  'note-lunch-v1':'Не забыть про обед. Эта запись его не заменит.',
  'note-grand-v1':'Записать спокойно. В торжественном тоне смесь не нуждается.',
  'note-self-legible-v1':'Главное, чтобы это смог прочесть я сам.',
  'note-spacing-v1':'Оставить место между строками. Буквам тоже нужен воздух.',
  'note-dry-paper-v1':'Бумагу держать сухой. Для жидкости есть банки.'
});
// Retained for frozen historical records, not eligible for new authoring.
const retired=new Set(['note-tomorrow-v1','note-legible-v1','note-drying-v1']);
export const authoringAsides=Object.freeze(Object.fromEntries(Object.entries(asides).filter(([id])=>!retired.has(id))));
