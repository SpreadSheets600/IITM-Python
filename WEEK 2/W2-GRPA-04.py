import math


def odd_num_check(number: int) -> str:
    return "yes" if number % 2 != 0 else "no"


def perfect_square_check(number: int) -> str:
    return "yes" if math.sqrt(number) == int(math.sqrt(number)) else "no"


def vowel_check(text: str) -> str:
    vowels = "aeiouAEIOU"
    return "yes" if any(char in vowels for char in text) else "no"


def divisibility_check(number: int) -> str:
    if number % 2 == 0 and number % 3 == 0:
        return "divisible by 2 and 3"
    elif number % 2 == 0:
        return "divisible by 2"
    elif number % 3 == 0:
        return "divisible by 3"
    else:
        return "not divisible by 2 and 3"


def palindrominator(text: str) -> str:
    return text + text[-2::-1]


def simple_interest(principal_amount: int, n_years: int) -> int:
    rate = 0.05 if n_years < 10 else 0.08
    interest = principal_amount * rate * n_years
    return round(interest)


def main():
    operation = input()

    if operation == "odd_num_check":
        number = int(input())
        print(odd_num_check(number))
    elif operation == "perfect_square_check":
        number = int(input())
        print(perfect_square_check(number))
    elif operation == "vowel_check":
        text = input()
        print(vowel_check(text))
    elif operation == "divisibility_check":
        number = int(input())
        print(divisibility_check(number))
    elif operation == "palindrominator":
        text = input()
        print(palindrominator(text))
    elif operation == "simple_interest":
        principal_amount = int(input())
        n_years = int(input())
        print(simple_interest(principal_amount, n_years))
    else:
        print("Invalid Operation")


if __name__ == "__main__":
    main()
