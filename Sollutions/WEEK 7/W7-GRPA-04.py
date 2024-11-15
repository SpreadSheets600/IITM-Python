def read_station_data():

    station_dict = {}
    n = int(input())

    for _ in range(n):

        train_name = input().strip()
        m = int(input())

        compartments = {}

        for _ in range(m):
            comp_name, passengers = input().split(",")
            compartments[comp_name.strip()] = int(passengers.strip())

        station_dict[train_name] = compartments

    return station_dict
