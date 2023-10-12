import unittest

from prime_numbers import prime_numbers
from roman_numerals_to_int import roman_numerals_to_int
from text_stat import text_stat


class TestPrimeNumbers(unittest.TestCase):
    """Тестирование программы prime_numbers."""

    def test_incorrect_values_1(self):
        self.assertEqual(prime_numbers('строка', True), [])

    def test_incorrect_values_2(self):
        self.assertEqual(prime_numbers(789, (1,)), [])

    def test_incorrect_values_3(self):
        self.assertEqual(prime_numbers(-5, -7.5), [])

    def test_incorrect_values_4(self):
        self.assertEqual(prime_numbers(-7.0, -5), [])

    def test_incorrect_values_5(self):
        self.assertEqual(prime_numbers(-2.4, 0), [])

    def test_incorrect_values_6(self):
        self.assertEqual(prime_numbers(9, 1.0), [])

    def test_correct_values_1(self):
        self.assertEqual(prime_numbers(5, 10), [5, 7])

    def test_correct_values_2(self):
        self.assertEqual(prime_numbers(2.1, 11), [3, 5, 7, 11])

    def test_correct_values_3(self):
        self.assertEqual(prime_numbers(-4.5, 8.8), [2, 3, 5, 7])


class TestRomanNumbers(unittest.TestCase):
    """Тестирование программы roman_numerals_to_int."""

    def test_incorrect_number_1(self):
        self.assertEqual(roman_numerals_to_int('XXIXX'), None)

    def test_incorrect_number_2(self):
        self.assertEqual(roman_numerals_to_int(''), None)

    def test_incorrect_number_3(self):
        self.assertEqual(roman_numerals_to_int('IIII'), None)

    def test_correct_number_1(self):
        self.assertEqual(roman_numerals_to_int('MDCLXVI'), 1666)

    def test_correct_number_2(self):
        self.assertEqual(roman_numerals_to_int('XXVIII'), 28)


class TestTextStat(unittest.TestCase):
    """Тестирование программы text_stat."""

    def test_incorrect_file_1(self):
        self.assertEqual(
            text_stat(1),
            {'error': 'Аргументом должна быть строка - название файла.'})

    def test_incorrect_file_2(self):
        self.assertEqual(
            text_stat('no_file.txt'),
            {'error': 'Файла с таким именем не существует.'})

    def test_correct_file(self):
        answer = {
                "a": (0, 0),
                "b": (0, 0),
                "c": (0, 0),
                "d": (2, 0.143),
                "e": (0, 0),
                "f": (0, 0),
                "g": (0, 0),
                "h": (0, 0),
                "i": (1, 0.071),
                "j": (0, 0),
                "k": (0, 0),
                "l": (0, 0),
                "m": (0, 0),
                "n": (0, 0),
                "o": (0, 0),
                "p": (0, 0),
                "q": (0, 0),
                "r": (0, 0),
                "s": (0, 0),
                "t": (0, 0),
                "u": (0, 0),
                "v": (0, 0),
                "w": (0, 0),
                "x": (0, 0),
                "y": (0, 0),
                "z": (0, 0),
                "а": (9, 0.429),
                "б": (2, 0.143),
                "в": (1, 0.071),
                "г": (0, 0),
                "д": (3, 0.214),
                "е": (7, 0.5),
                "ё": (1, 0.071),
                "ж": (0, 0),
                "з": (2, 0.143),
                "и": (3, 0.214),
                "й": (0, 0),
                "к": (3, 0.143),
                "л": (4, 0.286),
                "м": (2, 0.143),
                "н": (2, 0.143),
                "о": (2, 0.143),
                "п": (2, 0.143),
                "р": (3, 0.143),
                "с": (1, 0.071),
                "т": (5, 0.286),
                "у": (1, 0.071),
                "ф": (0, 0),
                "х": (0, 0),
                "ц": (1, 0.071),
                "ч": (1, 0.071),
                "ш": (0, 0),
                "щ": (1, 0.071),
                "ъ": (0, 0),
                "ы": (0, 0),
                "ь": (1, 0.071),
                "э": (0, 0),
                "ю": (0, 0),
                "я": (1, 0.071),
                "word_amount": 14,
                "paragraph_amount": 4,
                "bilingual_word_amount": 3}

        self.assertEqual(text_stat('text_file_example.txt'), answer)


if __name__ == '__main__':
    unittest.main()

