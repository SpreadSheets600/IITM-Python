# ==================== PART 1 ==================== #

import random

rolls = []
for i in range(100000):
    roll = random.randint(1, 6)
    rolls.append(roll)

count = 0
primes = [2, 3, 5]
for roll in rolls:
    if roll in primes:
        count += 1

print(f"COUNT : {count}")
print(f"LENGTH : {len(rolls)}")

some_var = count / len(
    rolls
)  # Some Var Represents The Probability Fo Rolling A Prime Number
print(f"PROBABILITY : {some_var}")

# ==================== PART 2 ==================== #

L = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
]  # List Of Non - Empty List Of Possitive Integers
S = 0

print("L : ", len(L))

for x in L:
    S += x  # Sum Of All Elements In L

flag = False
y = -1

for x in L:  # Looping Through All Elements In L
    if x * len(L) == S:  # If x * Length Of L Is Equal To S
        flag = True
        y = x  # y Is Equal To x
        print(f"Y : {y}")
        break  # Break The Loop


index_of_y = len(L) // 2
print(f"INDEX OF Y : {index_of_y}")

# ==================== PART 3 ==================== #

L = [90, 47, 8, 18, 10, 7]
S = [L[0]]
for i in range(1, len(L)):
    flag = True
    for j in range(len(S)):
        if L[i] < S[j]:
            before_j = S[:j]
            new_j = [L[i]]
            after_j = S[j:]

            S = before_j + new_j + after_j

            flag = False
            break
    if flag:
        S.append(L[i])
print(S)

# ==================== PART 4 ==================== #

point = [(3, 2), (0, 0)]
point = [(0, 0), (3, 2)]

points = []
for x in range(0, 5):
    for y in range(0, 5):
        points.append((x, y))

print(points)

for p in points:
    if p in point:
        print("YES")

# ==================== PART 5 ==================== #

L = [y - x for x in [1, 2, 3] for y in [3, 4, 5] if y > x]
print(L)

L = []
for x in [1, 2, 3]:
    for y in [3, 4, 5]:
        if y > x:
            L.append(y - x)

print(L)

# ==================== PART 6 ==================== #

triplets = [
    (x, y, z)
    for x in range(1, 100)
    for y in range(x + 1, 100)
    for z in range(y + 1, 100)
    if x**2 + y**2 == z**2
]

triplets = []
for x in range(1, 100):
    for y in range(x + 1, 100):
        for z in range(y + 1, 100):
            if x**2 + y**2 == z**2:
                triplets.append((x, y, z))


triplets = [
    (x, y, z)
    for x in range(1, 100)
    for y in range(1, 100)
    for z in range(1, 100)
    if x**2 + y**2 == z**2 and x < y < z
]

# ==================== PART 7 ==================== #

def some_function(word):
    space = " "
    if space in word:
        return False

    if not ("A" <= word[0] <= "Z"):
        return False
    for i in range(1, len(word)):
        if not ("a" <= word[i] <= "z"):
            return False
    return True

print(some_function('Riemann'))

# ==================== PART 8 ==================== #

def minmax(a, b):
    if a <= b:
        return a, b
    return b, a


print(minmax(3, 3))

# ==================== PART 9 ==================== #


def unique(L):
    L_uniq = []
    for elem in L:
        if elem not in L_uniq:
            L_uniq.append(elem)
    return L_uniq


def unique(L):
    L_uniq = []
    for elem in L:
        if elem not in L_uniq:
            L_uniq.append(elem)
    return L_uniq


# ==================== PART 10 ==================== #


def poly(L, x_0):
    psum = 0
    n = len(L)
    for i in range(1, n):
        psum = psum + L[i] * (x_0**i)
    return psum


# ==================== PART 11 ==================== #


def poly_zeros(L, a, b):
    zeros = []
    for x in range(a, b + 1):
        if poly(L, x) == 0:
            zeros.append(x)
    return zeros
