import csv


def get_goals(filename, country):
    """
    Get the count of players and their cumulative goals for this country

    Arguments:
        filename: string, path to the CSV file
        country: string, name of the country
    Return:
        result: tuple, (integer, integer)
    """
    num_players = 0
    num_goals = 0

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Country"] == country:
                num_players += 1
                num_goals += int(row["Goals"])

    if num_players == 0:
        return (-1, -1)

    return (num_players, num_goals)
