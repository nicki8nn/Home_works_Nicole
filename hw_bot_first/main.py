# У дужках вказали тип вхідних даних, а після -> тип того, що функція повертає
def parse_input(user_input: str) -> tuple:
    # .split() розбиваємо рядок на слова за пробілами
    parts = user_input.split()
    
    # Якщо ввели порожній рядок, повертаємо пусту команду і пустий список
    if len(parts) == 0:
        return "", []
    
    # Перше слово — це команда (cmd)
    cmd = parts[0].strip().lower()
    
    # Всі інші слова — це аргументи (args)
    args = parts[1:]
    
    return cmd, args

# Універсальна функція обробник (handler) для додавання контакту
def add_contact(args: list, contacts: dict) -> str:
    # Перевіряємо, чи передав користувач хоча б два аргументи (ім'я та номер)
    if len(args) < 2:
        return "Error: Give me name and phone please."
    
    # Розпаковуємо аргументи: перше слово в name, друге в phone
    name, phone = args

    # 2. Перевіряємо, чи номер складається з 10 цифр
    if not (phone.isdigit() and len(phone) == 10):
        return "Error: Phone number must contain exactly 10 digits (e.g., 0501234567)."
    
    # Зберігаємо дані у словник: ім'я стає ключем, номер — значенням
    contacts[name] = phone

    return "Contact added."

def change_contact(args: list, contacts: dict) -> str:
    # Перевірка на кількість аргументів
    if len(args) < 2:
        return "Error: Give me name and phone please."
    
    name, phone = args
    
    # ПЕРЕВІРКА: чи є такий контакт у словнику?
    if name not in contacts:
        return f"Error: Contact {name} not found."
    
    # Перевірка номера на 10 цифр (така ж як в add)
    if not (phone.isdigit() and len(phone) == 10):
        return "Error: New phone number must be 10 digits."
    
    # Якщо контакт є і номер правильний — оновлюємо
    contacts[name] = phone
    return "Contact updated."

def show_phone(args: list, contacts: dict) -> str:
    # 1. Перевірка чи ввів користувач ім'я
    if not args:
        return "Error: Give me a name."
    
    name = args [0]

    # 2. Перевірка чи є такий контакт у словнику
    if name in contacts:
        return contacts[name]
        return f"Error: Contact {name} not found."
    
def show_all_contacts(contacts: dict) -> str:
    # Перевірка чи словник не порожній
    if not contacts:
        return "Your contact list is empty."
    
    # Створюємо список рядків для кожного контакту.
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main() -> None:
    # 1. Створюємо словник для зберігання контактів (наша "база даних")
    contacts = {}

    # Виводимо вітальне повідомлення один раз при запуску
    print("Welcome to the assistant bot!")
    
    # Нескінченний цикл, щоб бот не вимикався
    while True:
        # Отримуємо текст від користувача
        user_input = input("Enter a command: ")
        
        # Розбираємо текст на команду та аргументи
        command, args = parse_input(user_input)

        # Перевірка на завершення роботи
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        # 1. Обробка команди hello
        elif command == "hello":
            print("How can I help you?")

        # 2. Обробка команди add
        elif command == "add":
            # Викликаємо функцію add_contact і друкуємо те, що вона поверне
            print(add_contact(args, contacts))

        # 3. Обробка команди change
        elif command == "change":
            print(change_contact(args, contacts))

        # 4. Обробка команди phone
        elif command == "phone":
            print(show_phone(args, contacts))

        # 5. Обробка команди show all
        elif command == "all":
            print(show_all_contacts(contacts))

        # Якщо команда не розпізнана
        else:
            print("Invalid command.")

# Запуск головної функції
if __name__ == "__main__":
    main()