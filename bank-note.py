# Deutsche Bank Banknote Verhoeff Algorithm

# Multiplication table (d table)
mult_table = [
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    (1, 2, 3, 4, 0, 6, 7, 8, 9, 5),
    (2, 3, 4, 0, 1, 7, 8, 9, 5, 6),
    (3, 4, 0, 1, 2, 8, 9, 5, 6, 7),
    (4, 0, 1, 2, 3, 9, 5, 6, 7, 8),
    (5, 9, 8, 7, 6, 0, 4, 3, 2, 1),
    (6, 5, 9, 8, 7, 1, 0, 4, 3, 2),
    (7, 6, 5, 9, 8, 2, 1, 0, 4, 3),
    (8, 7, 6, 5, 9, 3, 2, 1, 0, 4),
    (9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
]

# Inverse table (for check digit)
inverse = (0, 4, 3, 2, 1, 5, 6, 7, 8, 9)

# Permutation table (p table)
perm_table = [
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    (1, 5, 7, 6, 2, 8, 3, 0, 9, 4),
    (5, 8, 0, 3, 7, 9, 6, 1, 4, 2),
    (8, 9, 1, 6, 0, 4, 3, 5, 2, 7),
    (9, 4, 5, 3, 1, 2, 6, 8, 7, 0),
    (4, 2, 8, 6, 5, 7, 3, 9, 0, 1),
    (2, 7, 9, 3, 8, 0, 6, 4, 1, 5),
    (7, 0, 4, 6, 9, 1, 3, 2, 5, 8),
]

# Letter to digit mapping
letter_map = {
    "A": 0,
    "D": 1,
    "G": 2,
    "K": 3,
    "L": 4,
    "N": 5,
    "S": 6,
    "U": 7,
    "Y": 8,
    "Z": 9,
}


# Convert banknote string (digits + letters) to list of digits
def to_digits(banknote):
    digits = []
    for ch in banknote.upper():
        if ch.isdigit():
            digits.append(int(ch))
        elif ch in letter_map:
            digits.append(letter_map[ch])
        else:
            raise ValueError(f"Invalid character: {ch}")
    return digits


# Verhoeff algorithm
def verhoeff(number, validate=True):
    c = 0
    digits = to_digits(number)

    # If generating check digit, append 0
    if not validate:
        digits.append(0)

    # Apply σ^i permutation correctly
    for i, digit in enumerate(reversed(digits), start=1):
        c = mult_table[c][perm_table[(i - 1) % 8][digit]]

    if validate:
        return c == 0
    else:
        return inverse[c]


# User Interface
def main():
    print("\n=== Deutsche Bank Banknote Verhoeff Validator ===")
    print("1. Validate a banknote number")
    print("2. Generate a check digit for a banknote")

    choice = input("\nChoose an option (1 or 2): ").strip()

    if choice == "1":
        banknote = input("\nEnter the full banknote number: ").strip()
        try:
            if verhoeff(banknote, validate=True):
                print("Banknote is VALID.")
            else:
                print("Banknote is INVALID.")
        except ValueError as e:
            print(f"Error: {e}")

    elif choice == "2":
        base_number = input(
            "\nEnter the banknote number WITHOUT the check digit: "
        ).strip()
        try:
            check_digit = verhoeff(base_number, validate=False)
            print(f"Check digit: {check_digit}")
            print(f"Full banknote number: {base_number}{check_digit}")
        except ValueError as e:
            print(f"Error: {e}")

    else:
        print("Invalid choice.")


# Run program
if __name__ == "__main__":
    main()
