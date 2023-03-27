import re


def text_stat(filename: str) -> dict:
    """
    Главная функция анализа текста из файла.
    """
    try:
        with open(filename, encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        return {'error': 'Файла с таким именем не существует.'}
    except ValueError:
        return {'error': 'Аргументом должна быть строка - название файла.'}

    result = {}
    # заполянем словарь ключами - буквами алфавитов
    for key in map(chr, range(97, 123)):
        result[key] = (0, 0)
    for key in map(chr, range(1072, 1104)):
        result[key] = (0, 0)
    # если буквы есть в тексте, то меняем значение по ключу в словаре
    for letter, value in words_with_letter(text).items():
        if letter in result.keys():
            result[letter] = value
    result['word_amount'] = word_amount(text)
    result['paragraph_amount'] = paragraph_amount(text)
    result['bilingual_word_amount'] = bilingual_word_amount(text)
    return result


def bilingual_word_amount(text):
    """
    Функция считающая кол-во слов в тексте, состоящих из
    букв кириллического и латинского алфавитов.
    """
    count = 0
    for word in text.lower().split():
        russian_letter = False
        english_letter = False
        for symbol in word:
            if 97 <= ord(symbol) <= 122:  # диапзаон маленьких английских букв в ASCII таблице
                english_letter = True
            if 1072 <= ord(symbol) <= 1103:  # диапзаон маленьких русских букв в ASCII таблице
                russian_letter = True
        if english_letter and russian_letter:
            count += 1
    return count


def word_amount(text):
    """
    Функция подсчета слов в тексте.
    Словомм будем считать непустую строку, состоящую из букв латинского или
    кирилического алфавита или отдельное число.
    """
    text = re.sub(r'[^\w\s]', '', text)  # очищаем текст от знаков препинания 
    return len([word for word in text.split() if word.isalpha() or
                word.isalnum()])


def frequency_using_letter(text):
    """
    Функция подсчета кол-ва букв в тексте.
    """
    text = re.sub(r'[^\w\s]', '', text)
    result = {}
    for word in text.split():
        for letter in word.lower():
            result[letter] = result.get(letter, 0) + 1
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
        for word in re.sub(r'[^\w\s]', '', text).split():
            if key in word.lower():
                count += 1
        value = (value, count / word_amount(text))
        result[key] = value
    return result


def paragraph_amount(text):
    """
    Функция считающая кол-во абзацев в тексте.
    Абзацем будем считать строку, начинающуюся с табуляции или
    если между строками есть пустая, разедлительная строчка.
    """
    return text.count('\n\n') + text.count('\n\t') + text.count('\n    ') + 1
