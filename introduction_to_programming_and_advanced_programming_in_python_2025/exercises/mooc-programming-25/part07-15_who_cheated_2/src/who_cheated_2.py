# Write your solution here
def final_points():
    import csv
    from datetime import datetime, timedelta

    students = {}
    three_hours = timedelta(seconds = 3*60*60)

    with open("start_times.csv") as start:
        for line in csv.reader(start, delimiter = ";"):
            name       = line[0]
            start_time = datetime.strptime(line[1], "%H:%M")

            students[name] = {}
            students[name]["start_time"] = start_time
            students[name]["tasks"] = {}

    with open("submissions.csv") as sub:
        for line in csv.reader(sub, delimiter = ";"):
            name     = line[0]
            task     = int(line[1])
            points   = int(line[2])
            sub_time = datetime.strptime(line[3], "%H:%M")

            if sub_time - students[name]["start_time"] <= three_hours:
                if task not in students[name]["tasks"]:
                    students[name]["tasks"][task] = points
                else:
                    students[name]["tasks"][task] = max(students[name]["tasks"][task], points)
    final = {}
    for name in students:
        final[name] = sum(students[name]["tasks"].values())
    return final

if __name__  == "__main__":
    final = final_points()
    print(final)
