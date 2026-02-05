# write your solution here

if True:
    student_file   = input("Student information: ")
    exercise_file  = input("Exercises completed: ")
else:
    student_file  = "students1.csv"
    exercise_file = "exercises1.csv"

students = {}

with open(student_file) as new_file:
    for line in new_file:
        parts = line.split(";")
        id = parts[0]
        if id == "id": # ignore the header line
            continue
        full_name = parts[1] + " " + parts[2]
        students[id] = full_name.strip()

exercises = {}

with open(exercise_file) as new_file:
    for line in new_file:
        parts = line.split(";")
        id = parts[0]
        if id == "id": # ignore the header line
            continue
        exercises[id] = []
        for exercise in parts[1:]:
            exercises[id].append(int(exercise))

for id, student_name in students.items():
    if id in exercises:
        exercises_completed = sum(exercises[id])
        print(f" {student_name} {exercises_completed}")
    else:
        print(f"{student_name} 0")

# Student information: students1.csv
# Exercises completed: exercises1.csv
# pekka peloton 21
# jaana javanainen 27
# liisa virtanen 35