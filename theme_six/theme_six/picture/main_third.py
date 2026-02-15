import sys
from pathlib import Path
from colorama import init, Fore, Style

# 1. Вмикаємо кольори
init(autoreset=True)

def visualize_directory(path, indent=""):
    try:
        # Беремо список з папки
        items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        
        for item in items:
            # Ігноруємо папку venv, щоб не було "сміття" у виводі
            if item.name == "venv" or item.name.startswith("."):
                continue
                
            if item.is_dir():
                # Малюємо папку синім кольором
                print(f"{indent}{Fore.BLUE}{Style.BRIGHT} {item.name}/")
                # Йдемо вглиб (рекурсія)
                visualize_directory(item, indent + "    ")
            else:
                # Малюємо файл зеленим кольором
                print(f"{indent}{Fore.GREEN} {item.name}")
                
    except Exception as e:
        print(f"{indent}{Fore.RED}Помилка: {e}")

def main():
    # Перевіряємо, чи передали шлях
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Вкажіть шлях! Наприклад: python main_third.py .")
        return

    path = Path(sys.argv[1])

    if path.exists() and path.is_dir():
        print(f"{Fore.CYAN}Структура директорії {path.absolute()}:")
        visualize_directory(path)
    else:
        print(f"{Fore.RED}Шлях не знайдено або це не папка.")

if __name__ == "__main__":
    main()