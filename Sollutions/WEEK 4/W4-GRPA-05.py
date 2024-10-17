def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)


def total_cost(cart):
    return sum(quantity * price for quantity, price in cart)


def abbreviation(sentence):
    return ".".join(word[0].upper() for word in sentence.split()) + "."


def palindromes(words):
    return [word for word in words if word == word[::-1]]


def all_chars_from_big_words(sentence):
    return set(
        char.lower() for word in sentence.split() if len(word) > 5 for char in word
    )


def flatten(lol):
    return [item for sublist in lol for item in sublist]


def unflatten(items, n_rows):
    return [
        items[i : i + len(items) // n_rows]
        for i in range(0, len(items), len(items) // n_rows)
    ]


def make_identity_matrix(m):
    return [[1 if i == j else 0 for j in range(m)] for i in range(m)]


def make_lower_triangular_matrix(m):
    return [[j + 1 if j <= i else 0 for j in range(m)] for i in range(m)]
