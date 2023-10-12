from re import match


def is_roman_number(number: str) -> bool:
    """
    Функция проверки корректности записи римского числа.
    """
    reg_exp = r'^M{0,3}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$'
    if match(reg_exp, number) and number:
        return True
    return False


def roman_numerals_to_int(roman_numeral: str) -> int:
    """
    Функция перевода римских чисел в арабские (для чисел < 4000).
    """
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC',
             'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    if is_roman_number(roman_numeral):
        answer = 0
        for index, value in enumerate(roman_numeral):
            first_number = arabic[roman.index(value)]
            if len(roman_numeral) != index + 1:
                second_number = arabic[roman.index(roman_numeral[index + 1])]
            else:
                second_number = -1
            if first_number >= second_number:
                answer += first_number
            else:
                answer -= first_number
        return answer
    return None
