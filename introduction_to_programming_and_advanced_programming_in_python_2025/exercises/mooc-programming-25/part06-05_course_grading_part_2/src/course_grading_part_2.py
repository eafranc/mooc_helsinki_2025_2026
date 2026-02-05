# write your solution here
if True:
    student_file  = input("Student information: ")
    exercise_file = input("Exercises completed: ")
    exam_file     = input("Exam points: ")
else:
    student_file  = "students1.csv"
    exercise_file = "exercises1.csv"
    exam_file     = "exam_points1.csv"

students = {}

with open(student_file) as new_file:
    for line in new_file:
        parts = line.split(";")
        id = parts[0]
        if id == "id": # avoids the header line
            continue
        full_name = f"{parts[1]} {parts[2]}".strip()
        students[id] = full_name

exercises = {}

with open(exercise_file) as new_file:
    for line in new_file:
        parts = line.split(";")
        id = parts[0]
        if id == "id": # avoids the header line
            continue
        exercises[id] = []
        for exercise in parts[1:]:
            exercises[id].append(int(exercise))

exams = {}

with open(exam_file) as new_file:
    for line in new_file:
        parts = line.split(";")
        id = parts[0]
        if id == "id": # avoids the header line
            continue
        exams[id] = []
        for exam in parts[1:]:
            exams[id].append(int(exam))

"""
Calculates grades using boundaries pattern.

Boundaries represent the minimum points required for each grade:
- Grade 0: 0-14 points (fail)
- Grade 1: 15-17 points
- Grade 2: 18-20 points
- Grade 3: 21-23 points
- Grade 4: 24-27 points
- Grade 5: 28-30 points
"""
total_points_boundaries = [0, 15, 18, 21, 24, 28]

# Print tests to see every dictionary created:
# print(students)
# print(exercises)
# print(exams)

for id, full_name in students.items():
    if id in exercises:
        exercises_completed = sum(exercises[id])
        exercises_points    = exercises_completed // 4
    else:
        exercises_points = 0
    if id in exams: 
        exam_points = sum(exams[id])
    else:
        exam_points = 0
    total_points = exercises_points + exam_points

    for i in range(5,-1, -1): # Find appropriate grade (reverse loop: start from highest grade)
        if total_points >= total_points_boundaries[i]:
            print(f"{full_name} {i}")
            break

# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv
# pekka peloton 0
# jaana javanainen 1
# liisa virtanen 3


