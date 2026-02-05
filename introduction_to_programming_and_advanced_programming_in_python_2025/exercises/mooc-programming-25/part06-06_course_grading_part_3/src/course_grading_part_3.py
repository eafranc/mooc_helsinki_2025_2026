# tee ratkaisu tänne
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
        if id == "id": # avoids the header file
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
boundary_points = [0, 15, 18, 21, 24, 28]

name_h     = "name"
exec_nbr_h = "exec_nbr"
exec_pts_h = "exec_pts."
exm_pts_h  = "exm_pts."
tot_pts_h  = "tot_pts."
grade_h    = "grade"

print(f"{name_h: <30}{exec_nbr_h:10}{exec_pts_h:10}{exm_pts_h:10}{tot_pts_h:10}{grade_h:10}")
for id, full_name in students.items():
    if id in exercises:
        completed_exercises = sum(exercises[id])
        exercises_points    = completed_exercises // 4
    else:
        exercises_points     = 0
    if id in exams:
        exam_points = sum(exams[id])
    else:
        exam_points = 0
    total_points = exercises_points + exam_points

    for grade in range(5, -1, -1): # iteration from the biggest to the lowest grade
        if total_points >= boundary_points[grade]:
            print(f"{full_name: <30}{completed_exercises:<10}{exercises_points:<10}{exam_points:<10}{total_points:<10}{grade:<10}")
            break

# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv

# name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
# pekka peloton                 21        5         9         14        0
# jaana javanainen              27        6         11        17        1
# liisa virtanen                35        8         14        22        3
