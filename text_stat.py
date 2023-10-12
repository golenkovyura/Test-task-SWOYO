from re import sub
from string import ascii_lowercase
from collections import Counter


def text_stat(filename: str) -> dict:
    """
    Главная функция анализа текста из файла.
    """
    try:
        with open(filename, encoding='utf-8') as file:
            text = file.read().lower()
    except FileNotFoundError:
        return {'error': 'Файла с таким именем не существует.'}
    except ValueError:
        return {'error': 'Аргументом должна быть строка - название файла.'}

    result = {}
    # заполянем словарь ключами - буквами алфавитов
    for key in ascii_lowercase:
        result[key] = (0, 0)
    for key in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
        result[key] = (0, 0)
    # если буквы есть в тексте, то меняем значение по ключу в словаре
    for letter, value in words_with_letter(text).items():
        if letter in result.keys():
            result[letter] = value
    result['word_amount'] = word_amount(text)
    result['paragraph_amount'] = paragraph_amount(filename)
    result['bilingual_word_amount'] = bilingual_word_amount(text)
    return result


def bilingual_word_amount(text):
    """
    Функция считающая кол-во слов в тексте, состоящих из
    букв кириллического и латинского алфавитов.
    """
    count = 0
    for word in text.split():
        russian_letter = False
        english_letter = False
        for symbol in word:
            if symbol in ascii_lowercase:
                english_letter = True
            if symbol in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
                russian_letter = True
        if english_letter and russian_letter:
            count += 1
    return count


def word_amount(text):
    """
    Функция подсчета слов в тексте.
    Словом будем считать непустую строку, состоящую из букв латинского или
    кирилического алфавита или отдельное число.
    """
    text = sub(r'[^\w\s]', '', text)  # очищаем текст от знаков препинания
    return len([word for word in text.split() if word.isalpha() or
                word.isalnum()])


def frequency_using_letter(text):
    """
    Функция подсчета кол-ва букв в тексте.
    """
    text = sub(r'[^\w\s]', '', text)
    result = Counter(''.join(text.split()))
    return result


def words_with_letter(text):
    """
    Функция возвращает словарь, где ключ - буква, а
    значение - кортеж, где первый элемент - частота встречания
    буквы, а второй - доля слов из текста, в которых есть эта буква.
    """
    result = {}
    for key, value in frequency_using_letter(text).items():
        count = 0
        for word in sub(r'[^\w\s]', '', text).split():
            if key in word:
                count += 1
        value = (value, round(count / word_amount(text), 3))
        result[key] = value
    return result


def paragraph_amount(filename):
    """
    Функция считающая кол-во абзацев в тексте.
    """
    count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        rows = f.read().splitlines()
        for row in rows:  # Ищем первую непустую строку
            if len(row.strip()):
                first_row = rows.index(row)
                count += 1
                break

        array = rows[first_row + 1:]
        for index in range(len(array)):  # Начиная с непустой строки перебираем строки и считаем абзацы
            empty = False
            if index >= 1 and len(array[index - 1].strip()) == 0:
                empty = True
            if ((array[index].startswith(('\t', ' ', '\n')) or empty) and
                    len(array[index].strip())):
                count += 1
        return count
