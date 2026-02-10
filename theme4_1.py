from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Розраховує кількість днів між заданою датою (РРРР-ММ-ДД) і поточною датою.
    
    :param date: Рядок з датою у форматі 'YYYY-MM-DD'
    :return: Ціле число (різниця у днях)
    """
    try:
        # 1. Перетворюємо рядок у об'єкт datetime
        # Якщо формат неправильний, тут виникне ValueError
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        # 2. Отримуємо поточну дату (без годин та хвилин)
        today = datetime.today().date()
        
        # 3. Розраховуємо різницю. 
        # Згідно з умовою: якщо задана дата у майбутньому — результат від'ємний.
        # Тому віднімаємо від 'сьогодні' 'задану дату'.
        delta = today - given_date # Тут створюється об'єкт timedelta
        
        # 4. Повертаємо кількість днів як ціле число
        return delta.days 
    
    except ValueError:
        # Обробка випадку, коли рядок має неправильний формат
        print(f"Помилка: Рядок '{date}' не відповідає формату РРРР-ММ-ДД.")
        return None
    except TypeError:
        # Обробка випадку, коли передано не рядок
        print("Помилка: Вхідні дані мають бути рядком.")
        return None


if __name__ == "__main__":
    print(get_days_from_today("2020-10-09"))  # Минуле: поверне додатне число
    print(get_days_from_today("2027-01-01"))  # Майбутнє: поверне від'ємне число
    print(get_days_from_today("не-дата"))      # Помилка: виведе повідомлення і поверне None


