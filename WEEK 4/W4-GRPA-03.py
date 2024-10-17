min = None


def find_min(items: list):
    if not items:
        return None
    minimum = items[0]
    for item in items[1:]:
        if item < minimum:
            minimum = item
    return minimum


def odd_increment_even_decrement_no_modify(items) -> list:
    return [(x + 1 if x % 2 != 0 else x - 1) for x in items]


def odd_square_even_double_modify(items: list):
    for i in range(len(items)):
        if items[i] % 2 != 0:
            items[i] = items[i] ** 2
        else:
            items[i] = items[i] * 2


def more_than_two_unique_vowels(sentence):
    vowels = set("aeiou")
    result = set()
    words = sentence.split(",")
    for word in words:
        unique_vowels = set(char for char in word if char in vowels)
        if len(unique_vowels) > 2:
            result.add(word)
    return result


def sum_of_list_of_lists(lol):
    return sum(sum(lst) for lst in lol)


def flatten(lol):
    return [item for sublist in lol for item in sublist]


def all_common(strings):
    if not strings:
        return ""
    common_chars = set(strings[0])
    for s in strings[1:]:
        common_chars &= set(s)
    return "".join(sorted(common_chars))


def vocabulary(sentences):
    vocab = set()
    for sentence in sentences:
        words = sentence.lower().split()
        vocab.update(words)
    return vocab
