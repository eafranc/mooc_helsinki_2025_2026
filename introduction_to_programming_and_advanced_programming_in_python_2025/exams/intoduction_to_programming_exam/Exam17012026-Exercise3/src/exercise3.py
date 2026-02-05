# Write your solution to exercise 3 here
def read_points():
    with open("statistics.txt") as file:
        teams_results = []

        for line in file:
            line = line.strip()
            [team, status] = line.split(":")
            status = status.split("-")

            try:
                wins = int(status[0])
                losses = int(status[1])
                ties = int(status[2])
            except ValueError:
                raise ValueError(f"ValueError: Invalid format in the file: {line}")

            points = [3*wins, 0*losses, 1*ties]
            teams_results.append((team, sum(points)))

    return teams_results

if __name__ == "__main__":
    teams_res = read_points()
    print(teams_res)

# RESULTS:
# [('Heba hawks', 16), 
# ('Brewsters', 19), 
# ('Sleepers', 0), 
# ('KBC', 19), 
# ('Navy jerries', 22), 
# ('Loosisters', 24)]

# INCORRECT LINES FOR TEST:
# KBC:AAA-1-ll
# Loosisters:7-4.5-1
