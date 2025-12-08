# Overall Code for Verhoeff Algorithm

# First we will initialize the multiplication table
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

# We will write down the inverse of that number
inverse = (0, 4, 3, 2, 1, 5, 6, 7, 8, 9)

# We will then write out the permutation table
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


# With these finally set up we can write out the function
def verhoeff(number, validate=True, terse=True, verbose=False):
    """
    Runs Verhoeff algorithm where it validates if the number that user inputted is valid

    Args:
        number: An integer, the number that is getting checked
        validate: A boolean initially set to True
        terse: A boolean initially set to True
        verbose: A boolean initially set to False

    Returns:
        When in checksum mode it returns the expected correct checksum digit. When in validation
        mode it returns True if the last digit checks correctly. When in terse mode or in a single
        digit it will return True if it is valid (when the last digit is a correct check digit).
    """
