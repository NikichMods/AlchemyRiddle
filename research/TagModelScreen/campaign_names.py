# SPDX-License-Identifier: MPL-2.0
"""Original editorial names; no vanilla identities or recipes in this bank.

Exact visible signatures are authored here rather than inferred from poetry.
Complete phrases avoid a runtime Russian morphology engine. This is a first
reviewable bank, not human acceptance of every individual name.
"""
import random

VERSION = 1


def entry(role, tags, *names):
    return (role, frozenset(tags.split('|'))), names


REAGENT_NAMES = dict([
    entry('Powder', 'Insect|Mineral|Plant', 'Мука янтарного сада', 'Хрустящий гербарий'),
    entry('Powder', 'Dark|Insect|Plant', 'Помол ночной росянки', 'Пепел мухолова'),
    entry('Powder', 'Dark|Plant', 'Труха', 'Чёрный папоротник, тонкий помол'),
    entry('Powder', 'Corpse|Dark|Organ', 'Прах бессонного сердца', 'Посмертный помол'),
    entry('Powder', 'Insect|Mineral', 'Пыль каменного жука', 'Хитиновый мел'),
    entry('Powder', 'Plant', 'Вересковая мука', 'Сухой сад'),
    entry('Powder', 'Animal|Insect', 'Мотыльковый помол', 'Крошево жужелицы'),
    entry('Powder', 'Corpse|Mineral|Organ', 'Костяная соль', 'Мел последнего ребра'),
    entry('Powder', 'Fish', 'Чешуя, мелкий помол', 'Рыбья мука'),
    entry('Powder', 'Corpse', 'Останки', 'Прах безымянного', 'Тихая мука', 'Погребальная пыль'),
    entry('Powder', 'Mineral', 'Кварцевая мука', 'Прах колокола', 'Соль без моря',
          'Каменный сон', 'Мел расколотой башни', 'Шпат'),
    entry('Powder', 'Corpse|Mineral', 'Могильный мел', 'Пепел каменного гроба'),
    entry('Fluid', 'Corpse|Insect|Plant', 'Настой мёртвой мухоловки', 'Жидкий гербарий падальщика'),
    entry('Fluid', 'Dark|Insect|Slime', 'Ночная тягучесть', 'Сироп чёрного слизнежука'),
    entry('Fluid', 'Dark|Plant', 'Отвар ведьминого сада', 'Тень во флаконе'),
    entry('Fluid', 'Corpse|Dark|Organ|Slime', 'Посмертная патока', 'Липкий отвар сердца'),
    entry('Fluid', 'Insect|Plant|Slime', 'Нектар липкой росянки', 'Садовый клей мухолова'),
    entry('Fluid', 'Plant|Slime', 'Болотная патока', 'Зелёная тягучесть'),
    entry('Fluid', 'Animal|Insect', 'Жучиный рассол', 'Вытяжка сверчка'),
    entry('Fluid', 'Corpse|Insect|Organ|Plant', 'Отвар желудка садового падальщика', 'Последний нектар'),
    entry('Essence', 'Insect', 'Жужжание', 'Мотыльковый дух', 'Эхо стрекозы', 'Память сверчка'),
    entry('Essence', 'Dark|Plant|Slime', 'Липкая тень сада', 'Дыхание чёрной ряски'),
    entry('Essence', 'Dark|Plant', 'Сумеречный дух', 'Сон папоротника'),
    entry('Essence', 'Corpse|Dark|Organ|Slime', 'Душа забытого сердца', 'Посмертная тягучесть'),
    entry('Essence', 'Plant|Slime', 'Болотный сон', 'Память росянки', 'Тягучий дух', 'Шёпот ряски'),
    entry('Essence', 'Corpse|Insect|Organ|Plant', 'Дух сердца мухолова', 'Посмертный гербарий'),
    entry('Universal', 'Corpse', 'Покой', 'Останки без имени'),
    entry('Universal', 'Plant', 'Ведьмин лист', 'Садовая диковина'),
    entry('Universal', 'Corpse|Plant', 'Мёртвый цветок', 'Последний гербарий'),
    entry('Universal', 'Water', 'Подлёдная вода', 'Капля из старого колодца'),
])

# One explicit cosmetic exception in the manifest, not another frequency scorer.
IRONIC_SIGNATURE = ('Essence', frozenset({'Corpse', 'Dark', 'Organ', 'Slime'}))
IRONIC_NAME = 'Нежность'

TARGET_TITLES = (
    'Эликсир отложенного проклятия', 'Тихая поправка к мирозданию',
    'Малая милость', 'Настойка здравого сомнения', 'Почти благополучный опыт',
    'Бальзам для трудных понедельников', 'Отсрочка неизбежного', 'Последний довод алхимика',
    'Невредимый результат', 'Утешение № 7', 'Пара капель благоразумия', 'Мягкое возражение судьбе',
    'Чудо с оговорками', 'Скромное торжество', 'Эликсир второго мнения', 'Почти вечность',
    'Милость по протоколу', 'Приятная аномалия', 'Средство от дурных предзнаменований',
    'Право на ещё одну попытку', 'Небольшая дерзость', 'Доказательство чудес',
    'Завтрашнее облегчение', 'Доброе знамение, выдержанное', 'Случайная благодать',
    'Эликсир благоразумного риска', 'Починка обстоятельств', 'Учёное утешение',
    'Флакон приличной удачи', 'Возражение последней инстанции', 'Обходной путь',
    'Микстура умеренного чуда', 'Запасной рассвет', 'Договор с невероятным',
    'Неокончательный приговор', 'Лабораторная вежливость', 'Удача на испытательном сроке',
    'Теорема спокойного сна', 'Флакон добрых намерений', 'Малое нарушение порядка',
)


def target_names(target_ids, seed):
    """No answer, tag, relation or clue parameter is available to this function."""
    ids = sorted(target_ids)
    if len(ids) > len(TARGET_TITLES):
        raise ValueError('Target title bank exhausted')
    choices = list(TARGET_TITLES)
    random.Random(seed).shuffle(choices)
    return dict(zip(ids, choices))


def reagent_names(records, seed, allow_irony=True):
    rng = random.Random(seed)
    used, assigned = set(), {}
    irony_used = False
    for row in sorted(records, key=lambda r: r['id']):
        key = (row['type'], frozenset(row['tags']))
        if key not in REAGENT_NAMES:
            raise ValueError('Missing authored visible signature')
        choices = [s for s in REAGENT_NAMES[key] if s not in used]
        if allow_irony and not irony_used and key == IRONIC_SIGNATURE:
            name, irony_used = IRONIC_NAME, True
        elif choices:
            name = rng.choice(choices)
        else:
            raise ValueError('Reagent title bank exhausted; expand before release')
        assigned[row['id']] = name
        used.add(name)
    return assigned
