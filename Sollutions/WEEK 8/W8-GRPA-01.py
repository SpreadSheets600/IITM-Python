def get_freq(filename):
    """
    Extract frequency information from the file

    Argument:
        filename: string, path to file
    Return:
        result: dictionary; keys are strings, values are integers
    """
    result = {}

    with open(filename, "r") as file:
        for line in file:
            word = line.strip()
            if word in result:
                result[word] += 1
            else:
                result[word] = 1

    return result
