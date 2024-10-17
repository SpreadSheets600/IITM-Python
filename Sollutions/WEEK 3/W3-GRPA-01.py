with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

if task == "sum_until_0":
    total = 0
    n = int(input())
    while n != 0:  # the terminal condition
        total += n  # add n to the total
        n = int(input())  # take the next n from the input
    print(total)

elif task == "total_price":
    total_price = 0
    while True:  # repeat forever since we are breaking inside
        line = input()
        if line == "END":  # The terminal condition
            break
        quantity, price = line.split()  # split uses space by default
        quantity, price = int(quantity), int(price)  # convert to ints
        total_price += quantity * price  # accumulate the total price
    print(total_price)

elif task == "only_ed_or_ing":
    while True:
        word = input()
        if word == "STOP":  # terminal condition
            break
        if word.lower().endswith(("ed", "ing")):  # check the condition
            print(word)  # output the valid words

elif task == "reverse_sum_palindrome":
    while True:
        n = int(input())
        if n == -1:  # terminal condition
            break
        reversed_n = int(str(n)[::-1])  # reverse the number
        if str(n + reversed_n) == str(n + reversed_n)[::-1]:  # check if palindrome
            print(n)  # print the valid number

elif task == "double_string":
    while True:
        line = input()
        if line == "":  # terminal condition (empty line)
            break
        print(line * 2)  # print the line repeated twice

elif task == "odd_char":
    word = input()
    while word != word.endswith("."):
        odd_char = word[::2]
        print(odd_char, end=" ")
        word = input()

elif task == "only_even_squares":
    while True:
        line = input()
        if line == "NAN":  # terminal condition
            break
        number = int(line)  # convert to integer
        if number % 2 == 0:  # check if the number is even
            print(number**2)  # print the square of the number

elif task == "only_odd_lines":
    odd_lines = []
    count = 0
    while True:
        line = input()
        if line == "END":  # terminal condition
            break
        count += 1
        if count % 2 == 1:  # check if the line number is odd
            odd_lines.append(line)  # add to the list
    print("\n".join(reversed(odd_lines)))  # print odd lines in reverse order
