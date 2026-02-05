# Write your solution here
def add_student(students: dict, name: str):
    students[name] = {"courses": []} # students[name] = {"course": []}

def add_course(students: dict, name: str, course: tuple):
    students[name]["courses"].append(course)

def print_student(students: dict, name: str):
    if name in students:
        print(f"{name}:")
        valid_courses = {} # valid_courses[course_name] = course_grade
        count_valid_courses = 0
        for course_name, course_grade in students[name]["courses"]:
            if course_grade == 0:
                continue
            if course_name in valid_courses:
                if course_grade > valid_courses[course_name]:
                    valid_courses[course_name] = course_grade
            else:
                valid_courses[course_name] = course_grade
                count_valid_courses += 1
        if count_valid_courses != 0:
            print(f" {count_valid_courses} completed courses:")
        else:
            print(" no completed courses")
        sum_grade     = 0
        count_grade   = 0
        for course_name, course_grade in valid_courses.items():
            print(f"  {course_name} {course_grade}")
            sum_grade   += course_grade
            count_grade += 1
        if count_grade != 0:
            print(f" average grade {sum_grade / count_grade}")
    else:
        print(f"{name}: no such person in the database")

def summary(students: dict):
    student_summary = {} # student_summary[name] = {"no_valid_courses": int, "average_grade": int}
    for name, courses in students.items():
        student_summary[name] = {"no_valid_courses": 0, "average_grade": 0} # initialize dictionary student_summary (2 levels dict!)
        # Repeat same pattern from print_student()
        valid_courses = {} # valid_courses[course_name] = course_grade
        # count_valid_courses = 0
        for course_name, course_grade in students[name]["courses"]:
            if course_grade == 0:
                continue
            if course_name in valid_courses:
                if course_grade > valid_courses[course_name]:
                    valid_courses[course_name] = course_grade
            else:
                valid_courses[course_name] = course_grade
                student_summary[name]["no_valid_courses"] += 1
        # print(f"{count_valid_courses} completed courses:")
        sum_grade     = 0
        count_grade   = 0
        for course_name, course_grade in valid_courses.items():
            # print(f"{course_name} {course_grade}")
            sum_grade   += course_grade
            count_grade += 1
        # print(f"average grade {sum_grade / count_grade}")
        student_summary[name]["average_grade"] = sum_grade / count_grade

    best_student_no_valid_courses = ""
    best_no_valid_courses         = 0
    best_student_average_grade    = ""
    best_average_grade            = 0
    for name, value in student_summary.items():
        if value["no_valid_courses"] > best_no_valid_courses:
            best_no_valid_courses         = value["no_valid_courses"]
            best_student_no_valid_courses = name
        if value["average_grade"] > best_average_grade:
            best_average_grade         = value["average_grade"]
            best_student_average_grade = name
    # STUDENTS' DATABASE STATISTICS
    print(f"students {len(students)}")
    print(f"most courses completed {best_no_valid_courses} {best_student_no_valid_courses}")
    print(f"best average grade {best_average_grade} {best_student_average_grade}")

if __name__ == "__main__":
    # students = {}
    # add_student(students, "Peter")
    # add_student(students, "Eliza")
    # print_student(students, "Peter")
    # print_student(students, "Eliza")
    # print_student(students, "Jack")
# Peter:
#  no completed courses
# Eliza:
#  no completed courses
# Jack: no such person in the database

    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # print_student(students, "Peter")
# Peter:
#  2 completed courses:
#   Introduction to Programming 3
#   Advanced Course in Programming 2
#  average grade 2.5

    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    # add_course(students, "Peter", ("Introduction to Programming", 2))
    # print_student(students, "Peter")
# Peter:
#  2 completed courses:
#   Introduction to Programming 3
#   Advanced Course in Programming 2
#  average grade 2.5

    # students = {}
    # add_student(students, "Peter")
    # add_student(students, "Eliza")
    # add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    # add_course(students, "Peter", ("Introduction to Programming", 1))
    # add_course(students, "Peter", ("Advanced Course in Programming", 1))
    # add_course(students, "Eliza", ("Introduction to Programming", 5))
    # add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    # summary(students)
# students 2
# most courses completed 3 Peter
# best average grade 4.5 Eliza

    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 0))
    print_student(students, "Peter")
# Peter:
#  no completed courses