import re

def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує номер телефону до стандартного формату +380XXXXXXXXX.
    
    >>> normalize_phone("067\\t123 4567")
    '+380671234567'
    >>> normalize_phone("(095) 234-5678\\n")
    '+380952345678'
    >>> normalize_phone("+380 44 123 4567")
    '+380441234567'
    >>> normalize_phone("380501234567")
    '+380501234567'
    >>> normalize_phone("    +38(050)123-32-34")
    '+380501233234'
    """

    cleaned = re.sub(r'\D', '', phone_number)
# Використовуємо \D для видалення всього, крім цифр


    if cleaned.startswith('380'):
        return '+' + cleaned
    elif cleaned.startswith('0'):
        return '+38' + cleaned  # Додаємо +38, оскільки нуль вже є в 'cleaned'
    else:
        return '+380' + cleaned
    
    return normalized

# Тестові дані
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

if __name__ == "__main__":
    # Запуск doctest для перевірки ідеальності роботи
    import doctest
    doctest.testmod()

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
