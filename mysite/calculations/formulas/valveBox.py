def val_for_cost(company, letter, number, color):
    """ Функція повертає значення за метер квадратний картону з даними параметрами, або нуль, якщо такого ящика нема """

    # Перевірка на правильність компанії (Це скоріше на час розробки, бо користувач не вводить компанію)
    if company not in ('ПКПФ', 'ІСОПАК', 'ПРИДНІПРОВСЬКИЙ', 'ЛКПФ', 'ГЕЛІУС'):
        raise ValueError('Десь не сходяться назви компаній')

    # Інформація з бази данних про дану компанію
    # data20, data30 = read_price_from_db(company)

    # Формат параметрів для знаходження потрібного рядка
    params = f'{number}{color}'

    # Визначення потірбного стовпчика
    if letter in ('C', 'BC'):
        column = -3
    elif letter in ('B', 'EC'):
        column = -2
    elif letter in ('E', 'EB'):
        column = -1
    else:
        raise ValueError('Десь не співпадає профіль')

    # Витягування значення із 20-ї таблиці
    if int(number) in range(20, 27):
        for row in data20:
            if row[1] == params:
                return row[column]

    # Витягування значення із 30-ї таблиці
    elif int(number) in range(30, 35):
        for row in data30:
            if row[1] == params:
                return row[column]
    else:
        raise ValueError('Десь не співпадає марка')


def val_for_meter(letter, number, color):
    """ Функція повертає значення за метер квадратний картону з даними параметрами, або нуль, якщо такого ящика нема """

    return 20


def get_square(profil: str, length: int, width: int, height: int) -> float:
    """ Повертає площу на основі розміру коробки та профілю """
    if profil not in ('E', 'B', 'C', 'EB', 'EC', 'BC'):
        raise ValueError(f'Profil must be E, B, C, EB, EC or BC. Profil: {profil}')

    # Додаткові змінні
    num1: int = 40  # 40, 50
    num2: int = 4  # 4, 6, ... , 14, 16

    # Визначаємо перше число
    if profil in ('E', 'B', 'C'):
        num1 = 40
    if profil in ('EB', 'EC', 'BC'):
        num1 = 50

    # Визначаємо друге число
    if profil == 'E':
        num2 = 4
    if profil == 'B':
        num2 = 6
    if profil == 'C':
        num2 = 8
    if profil == 'EB':
        num2 = 12
    if profil == 'EC':
        num2 = 14
    if profil == 'BC':
        num2 = 16

    # Обраховуємо площу
    return ((length + width) * 2 + num1) * (width + height + num2) / 1000000


def prof(profil):
    """
    Приймає профіль (тей, що вводиться користувачем)
    Повертає значення профілю згину (наскільки я пам'ятаю)
    """
    if profil == 'E':
        return 4
    elif profil == 'B':
        return 6
    elif profil == 'C':
        return 8
    elif profil == 'EB':
        return 12
    elif profil == 'EC':
        return 14
    elif profil == 'BC':
        return 16


def zag(length, width, height, prof, shar):
    """
    Приймає розмір коробки і значення вище наведенної функції усе у (int)
    Повертає рядок з розмірами заготовки
    """
    if shar == 'Т':
        len_zag = int((length + width) * 2 + 40)
    else:
        len_zag = int((length + width) * 2 + 50)

    wid_zag = int(width + height + prof)

    # Те, що в центрі рельовки
    center_rel = int(height + prof / 2)

    # Якщо не парне число, віднімаємо 1 міліметр від ширини заготовки
    if (wid_zag - center_rel) % 2 != 0:
        wid_zag -= 1

    # Бокові рельовки
    side_rel = int((wid_zag - center_rel) / 2)

    # Усі рельовки
    rel = f'( {side_rel} / {center_rel} / {side_rel} )'

    return f'{len_zag} x {wid_zag} {rel}'


def cost(square, letter, number, color, printing, company):
    """
    Приймає площу (float), профіль (str), марку (str) та колір (str) та друк (str)
    Повертає собівартість за формулою (float)
    """

    # Друк
    if printing == '0':
        pr = 0
    elif printing == '1':
        pr = 0.1
    elif printing == '2':
        pr = 0.2
    else:
        pr = 1.4 * square

    # Робота (параметер вводиться користувачем)
    work = 1

    # Ціна, яку вводив користувач для даних параметрів
    value = val_for_cost(company, letter, number, color)

    # Якщо ціна не була введена в базу, то повертається 0
    if value == 0:
        return 0
    else:
        return square * value + (square * work) + pr