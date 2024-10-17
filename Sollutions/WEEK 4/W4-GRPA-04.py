def swap_halves(items):
    mid = len(items) // 2
    return items[mid:] + items[:mid]


def swap_at_index(items, k):
    return items[k + 1 :] + items[: k + 1]


def rotate_k(items, k=1):
    k = k % len(items)
    return items[-k:] + items[:-k]


def first_and_last_index(items, elem):
    first = items.index(elem)
    last = len(items) - 1 - items[::-1].index(elem)
    return (first, last)


def reverse_first_and_last_halves(items):
    mid = len(items) // 2
    items[:mid] = reversed(items[:mid])
    items[mid:] = reversed(items[mid:])
