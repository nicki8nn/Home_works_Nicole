# def get_upcoming_birthdays:
# users = ["Name": "Nicole", "Birthday": "2026-10-21"]
# import datetime


from datetime import datetime, date, timedelta

users = [
    {"name": "Nicole", "birthday": "2026-10-21"},
    {"name": "Alex", "birthday": "2025-06-13"},
    {"name": "Nina", "birthday": "2026-02-10"}
]

def get_upcoming_birthdays(users):
    today = date.today()
    end_day = today + timedelta(days=7)
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y-%m-%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        if not (today <= birthday_this_year <= end_day):
            continue

        congratulation_date = birthday_this_year

        weekday = congratulation_date.weekday()
        if weekday == 5:
            congratulation_date += timedelta(days=2)
        elif weekday == 6:
            congratulation_date += timedelta(days=1)
        result.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime("%Y-%m-%d")
        })

    return result
print(get_upcoming_birthdays(users))

