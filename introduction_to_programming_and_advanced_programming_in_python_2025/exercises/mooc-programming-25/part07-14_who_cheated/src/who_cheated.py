# Write your solution here
def get_students_info():
    import csv
    from datetime import datetime, timedelta

    students = {}
    with open("start_times.csv") as start_file:
        for line in csv.reader(start_file, delimiter=";"):
            name       = line[0]
            start_time = datetime.strptime(line[1], "%H:%M")

            students[name] ={
                "start_time": start_time,
                "tasks"     : [],
                "points"    : [],
                "sub_time"  : []
            }

    with open("submissions.csv") as sub_file:
        for line in csv.reader(sub_file, delimiter=";"):
            name     = line[0]
            task     = int(line[1])
            points   = int(line[2])
            sub_time = datetime.strptime(line[3], "%H:%M")

            students[name]["tasks"].append(task)
            students[name]["points"].append(points)
            students[name]["sub_time"].append(sub_time)
    return students

def cheaters():
    from datetime import datetime, timedelta
    students = get_students_info()
    list_of_cheaters = []
    three_hours = timedelta(seconds = 3*60*60)
    for name in students:
        for i in range(len(students[name]["sub_time"])):
            if (students[name]["sub_time"][i] - students[name]["start_time"]) > three_hours:
                list_of_cheaters.append(name)
                break
    return list_of_cheaters

if __name__ == "__main__":
    students = get_students_info()
    diff = students["matti"]["sub_time"][0] - students["matti"]["start_time"]
    print(diff)

    lst_cheaters = cheaters()
    print(lst_cheaters)


