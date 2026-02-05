# 1 - BEST SOLUTION - REFACTORING SOLUTION 2 (BELOW)
def get_exam_points_and_exercises():
    """Collects student data (exam points and exercises completed)"""
    data = []
    while True:
        line = input("Exam points and exercises completed: ").split()
        if len(line) == 0:
            break
        # Convert to int immediately to avoid repeated conversions later
        exam = int(line[0])
        exercises = int(line[1])
        data.append([exam, exercises])
    return data

def calculate_points_average(data):
    """Calculates average of total points (exam + exercise points)"""
    total_points = 0
    for exam, exercises in data:
        exercise_points = exercises // 10
        total_points += exam + exercise_points
    return total_points / len(data)

def grades_distribution(data):
    """
    Calculates grade distribution using boundaries pattern.
    
    Boundaries represent the minimum points required for each grade:
    - Grade 0: 0-14 points (fail)
    - Grade 1: 15-17 points
    - Grade 2: 18-20 points
    - Grade 3: 21-23 points
    - Grade 4: 24-27 points
    - Grade 5: 28-30 points
    """
    grades = [0] * 6
    boundaries = [0, 15, 18, 21, 24, 28]  # Minimum points for each grade
    
    for exam, exercises in data:
        exercise_points = exercises // 10
        total = exam + exercise_points
        
        # Special rule: less than 10 exam points = automatic fail
        if exam < 10:
            grades[0] += 1
        else:
            # Find appropriate grade (reverse loop: start from highest grade)
            for i in range(5, -1, -1):
                if total >= boundaries[i]:
                    grades[i] += 1
                    break  # Stop once grade is found
    
    return grades

def calculate_pass_percentage(grades):
    """Calculates pass percentage (all grades except 0)"""
    total = sum(grades)
    passed = total - grades[0]  # Everyone except grade 0
    return 100 * passed / total

def print_statistics(avg, pass_pct, grades):
    """Prints formatted statistics"""
    print("Statistics:")
    print(f"Points average: {avg:.1f}")
    print(f"Pass percentage: {pass_pct:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        print(f"  {i}: {'*' * grades[i]}")

def main():
    # Collect data
    data = get_exam_points_and_exercises()
    
    # Calculate statistics
    avg = calculate_points_average(data)
    grades = grades_distribution(data)
    pass_pct = calculate_pass_percentage(grades)
    
    # Display results
    print_statistics(avg, pass_pct, grades)

main()

# 2 - MY FIRST SOLUTION - VERBOSE, BUT GETS THE JOB DONE
# def get_exam_points_and_exercises():
#     list_of_exam_points_and_exercises = []
#     while True:
#         # Exam points: 0 - 20
#         # Exercises  : 0 - 100
#         line = input("Exam points and exercises completed: ").split()
#         if (len(line) == 0):
#             break
#         list_of_exam_points_and_exercises.append(line)
#     return list_of_exam_points_and_exercises

# def points_average(ls: list[list]):
#     exam_points     = 0
#     exercise_points = 0
#     students        = 0
#     for l in ls:
#         exam_points     += int(l[0])
#         exercise_points += (int(l[1])//10)
#         students        += 1
#     total_points   = exam_points + exercise_points
#     average_points = total_points/students
#     print(f"Points average: {average_points:.1f}")

# def grades_distribution(ls: list[list]):
#     grades = ["", "", "", "", "", ""]

#     exam_points     = 0
#     exercise_points = 0
#     for l in ls:
#         exam_points     = int(l[0])
#         exercise_points = (int(l[1])//10)
#         total_points  = exam_points + exercise_points

#         if exam_points < 10:
#             grades[0] += "*"
#         elif  0 <= total_points <= 14:
#             grades[0] += "*"
#         elif 15 <= total_points <= 17:
#             grades[1] += "*"
#         elif 18 <= total_points <= 20:
#             grades[2] += "*"
#         elif 21 <= total_points <= 23:
#             grades[3] += "*"
#         elif 24 <= total_points <= 27:
#             grades[4] += "*"
#         elif 28 <= total_points <= 30:
#             grades[5] += "*"
#     return grades

# def print_grades_analytics(grades):
#     print("Pass percentage: ", end = "")
#     total_grades = 0
#     total_fail   = len(grades[0])
#     for i in range(len(grades)):
#         total_grades += len(grades[i])
#     pass_percentage = (total_grades - total_fail)*(100)/(total_grades)
#     print(f"{pass_percentage:.1f}")

#     print("Grade distribution:")
#     for j in range(len(grades) -1, -1, -1):
#         print(f"{j}: {grades[j]}")

# def main():
#     list_exam_points_and_exercises = get_exam_points_and_exercises()
#     print("Statistics:")
#     points_average(list_exam_points_and_exercises)
#     grades_dist = grades_distribution(list_exam_points_and_exercises)
#     print_grades_analytics(grades_dist)

# main()
# ========================================================================
# SAMPLE OUTPUT
# Exam points and exercises completed: 15 87
# Exam points and exercises completed: 10 55
# Exam points and exercises completed: 11 40
# Exam points and exercises completed: 4 17
# Exam points and exercises completed:
# Statistics:
# Points average: 14.5
# Pass percentage: 75.0
# Grade distribution:
#   5:
#   4:
#   3: *
#   2:
#   1: **
#   0: *