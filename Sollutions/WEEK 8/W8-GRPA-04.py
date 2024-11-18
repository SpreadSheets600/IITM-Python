import csv


def num_to_words(mat):
    """
    Convert matrix to file

    Argument:
        mat: list of lists, matrix of single digit numbers
    Return:
        None
    """
    num_words = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }

    with open("words.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for i, row in enumerate(mat):
            words_row = [num_words[num] for num in row]
            if i == len(mat) - 1:
                writer.writerow(words_row)
            else:
                writer.writerow(words_row)
