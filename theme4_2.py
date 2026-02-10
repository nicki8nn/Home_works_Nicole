import random

def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> list[int]:
    """
    Генерує відсортований список унікальних випадкових чисел у заданому діапазоні.
    
    Параметри:
    - min_val: мінімальне число (>= 1)
    - max_val: максимальне число (<= 1000)
    - quantity: кількість чисел для вибору
    """
    
    # 1. Перевірка базових обмежень за умовою завдання
    if min_val < 1 or max_val > 1000:
        return []
    
    # 2. Чи min не більше max
    if min_val > max_val:
        return []
    
    # 3. Перевірка: чи кількість запитуваних чисел не перевищує розмір діапазону
    # quantity має бути позитивним числом
    if quantity <= 0 or quantity > (max_val - min_val + 1):
        return []

    try:
        # random.sample для генерації унікальних чисел.
        numbers = random.sample(range(min_val, max_val + 1), quantity)
        return sorted(numbers)
    except (ValueError, TypeError):
        # на випадок некоректних типів даних
        return []


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print(f"Ваші лотерейні числа: {lottery_numbers}")
    
    # Перевірка помилкових даних
    print(f"Помилка (min > max): {get_numbers_ticket(50, 10, 5)}")
    print(f"Помилка (некоректна кількість): {get_numbers_ticket(1, 36, 40)}")