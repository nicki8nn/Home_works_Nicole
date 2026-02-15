import pathlib
from typing import List, Dict

def get_cats_info(path: str) -> List[Dict[str, str]]:
    cats_list = []
    try:
        # 1. Працюємо з об'єктом Path
        file_path = pathlib.Path(path)
        
        # 2. Перевірка на існування
        if not file_path.exists():
            print(f"Помилка: Файл '{path}' не знайдено.")
            return []

        # 3. Читання файлу
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip() # Кожен рядок треба очистити від невидимих символів переносу (strip)
                if line:  # Якщо рядок не порожній
                    # Розбиваємо дані. дані потрібні окремо
                    cat_id, name, age = line.split(',')
                    # Створюємо словник
                    cat_dict = {
                        "id": cat_id, 
                        "name": name, 
                        "age": age
                    }
                    # Додаємо в список
                    cats_list.append(cat_dict)
                    
        return cats_list

    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []

if __name__ == "__main__":
    # Створюємо шлях до файлу
    path_to_file = pathlib.Path(__file__).parent / "text.txt"

    # Викликаємо функцію
    cats_info = get_cats_info(str(path_to_file))
    
    # Виводимо результат
    print(cats_info)