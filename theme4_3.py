raw_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

normalized_numbers = []

for phone_number in raw_numbers:
    
    digits = "". joint(char for char in phone_number if char.isdigit())

    if digits.startswith("380"):
        normalized = "+" + digits
    elif digits.startswith("0"):
        normalized = "+38" + digits
    else:
        normalized = "+380" + digits

    normalized_numbers.append(normalized)

print(normalized_numbers)