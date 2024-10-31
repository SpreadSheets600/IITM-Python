# mapping without loops or if statements
def is_greater_than_5(numbers: list) -> list:
    """Given a list of numbers, return a list of bools corresponding to whether the number is greater than 5"""
    return list(map(lambda x: x > 5, numbers))


# filtering without loops or if statements
def filter_less_than_5(numbers: list) -> list:
    """Given a list of numbers, return a list of numbers that are less than 5"""
    return list(filter(lambda x: x < 5, numbers))


# aggregation with filtering without loops or if statements
def sum_of_two_digit_numbers(numbers: list):
    """Given a list of numbers, find the sum of all two-digit numbers."""
    return sum(filter(lambda x: 10 <= x <= 99, numbers))


# aggregation with mapping without loops or if statements
def is_all_has_a(words: list) -> bool:
    """Given a list of words, check if all words have the letter 'a' (case insensitive) in it."""
    return all(map(lambda word: "a" in word.lower(), words))


# enumerate
def print_with_numbering(items):
    """
    Print a list in multiple lines with numbering.
    Eg. ["apple","orange","banana"]
    1. apple
    2. orange
    3. banana
    """
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")


# zip
def parallel_print(countries, capitals):
    """
    Print the countries and capitals in multiple line seperated by a hyphen with space around it.
    """
    for country, capital in zip(countries, capitals):
        print(f"{country} - {capital}")


# key value list to dict
def make_dict(keys, values):
    """Create a dict with keys and values"""
    return dict(zip(keys, values))


# enumerate with filtering and map without comprehensions
def indices_of_big_words(words) -> list:
    """Given a list of words, find the indices of the big words (length greater than 5)."""
    return list(map(lambda x: x[0], filter(lambda x: len(x[1]) > 5, enumerate(words))))


# zip with mapping and aggregation without comprehensions
def decode_rle(chars: str, repeats: list) -> str:
    """
    Create a string with i-th char from chars repeated i-th value of repeats number of times.

    Note rle refers to Run-length encoding.
    """
    return "".join(map(lambda x: x[0] * x[1], zip(chars, repeats)))
