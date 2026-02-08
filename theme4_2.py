import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        return []
    if quantity > (max - min + 1):
        return []
    numbers = set()
    while len(numbers) < quantity:
        number = random.randint(min, max)
        numbers.add(number)
    return sorted(numbers)
print(get_numbers_ticket(1,36,5))
