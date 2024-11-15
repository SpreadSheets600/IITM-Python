teams = ["CSK", "DC", "KKR", "MI", "PK", "RR", "RCB", "SH"]

points_table = {team: 0 for team in teams}

for i in range(8):

    match_data = input().strip().split(",")

    winner = match_data[0]
    points = len(match_data) - 1

    points_table[winner] += points

sorted_teams = sorted(points_table.items(), key=lambda x: (-x[1], x[0]))

for team, wins in sorted_teams:
    print(f"{team}:{wins}")
