import pathlib
from typing import Tuple

def total_salary(path: str) -> Tuple[int, int]:
    """
    Аналізуємо файл із зарплатами та повертаємо загальну та середню суму.
    
    >>> # Приклад рядка у файлі: Alex Korp,3000
    """
    total = 0
    count = 0
    
    try:
        # Перетворюємо рядок шляху на об'єкт Path
        file_path = pathlib.Path(path)
        
        # Перевірка на існування файлу
        if not file_path.exists():
            print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
            return 0, 0

        # Відкриваємо файл із вказанням кодування для кирилиці
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    # Розділяємо рядок комою. Ім'я ігноруємо (_), беремо лише зарплату
                    _, salary = line.split(',')
                    total += int(salary)
                    count += 1
        
        # Рахування середньої зарплати (цілочисельне ділення)
        average = total // count if count > 0 else 0
        
        return total, average

    except ValueError:
        print(f"Помилка: Дані у файлі '{path}' мають невірний формат.")
        return 0, 0
    except Exception as e:
        print(f"Сталася непередбачувана помилка: {e}")
        return 0, 0

if __name__ == "__main__":
    # Автоматично знаходимо файл поруч із main.py
    # __file__ - це шлях до цього скрипта, .parent - папка, де він лежить
    path_to_file = pathlib.Path(__file__).parent / "text_file.txt"
    
    # Виклик функції (передаємо шлях як рядок)
    total, average = total_salary(str(path_to_file))
    

    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")