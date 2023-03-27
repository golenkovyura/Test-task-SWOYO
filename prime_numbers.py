from math import ceil


def eratosthene(n: int) -> list:
    """
    Функция, реализующая алгоритм решета Эратосфена,
    возврщающая список всех простых чисел от 2 до n.
    """
    numbers = list(range(n + 1))
    if len(numbers) > 1:
        numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = False
    return [number for number in numbers if number]


def prime_numbers(low: int, high: int) -> list:
    """
    Функция, возвращающая список простых чисел
    в заданном диапазоне.
    """
    if (isinstance(low, (int, float)) and  # проверка корректности данных
            isinstance(high, (int, float)) and
            low <= high):
        return [elem for elem in eratosthene(int(high)) if elem >= ceil(low)]
    return []
