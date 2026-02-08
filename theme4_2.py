import random

def get_numbers_ticket(min: int, max: int, quantity: int) ->list[int]:
    """
    Генерує відсортований список унікальних випадкових чисел у заданому діапазоні.

    >>> isinstance(get_numbers_ticket(1, 49, 6), list)
    True
    >>> len(get_numbers_ticket(1, 49, 6))
    6
    >>> get_numbers_ticket(1, 10, 11)
    []
    >>> get_numbers_ticket(0, 100, 5)
    []
    """
    if min < 1 or max > 1000:
        return []
    if quantity > (max - min + 1):
        return []
    numbers = set()
    while len(numbers) < quantity:
        number = random.randint(min, max)
        numbers.add(number)
    return sorted(numbers)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

print(get_numbers_ticket(1,36,5))
