# tee ratkaisusi tänne
class Course:
    def __init__(self, name):
        self.name    = name
        self.grade   = 0
        self.credits = 0

    def __str__(self):
        return f"{self.name} ({self.credits} cr) grade {self.grade}"

    @property # getter
    def name(self):
        return self.__name

    @name.setter # setter
    def name(self, name: str):
        if name != "":
            self.__name = name
        else:
            raise ValueError("Course name cannot be empty")

    @property # getter
    def grade(self):
        return self.__grade

    @grade.setter # setter
    def grade(self, grade: int):
        if grade >= 0:
            self.__grade = grade

    @property # getter
    def credits(self):
        return self.__credits

    @credits.setter # setter
    def credits(self, credits: int):
        if credits >= 0:
            self.__credits = credits

    def add_credits(self, credits: int):
        self.credits = credits

    def add_grade(self, grade: int):
        if self.grade < grade:
            self.grade = grade

class CourseRecord:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if not name in self.__courses:
            self.__courses[name] = Course(name)
        self.__courses[name].add_grade(grade)
        self.__courses[name].add_credits(credits)

    def get_course_data(self, name: str):
        if not name in self.__courses:
            return None
        else:
            return self.__courses[name]

    def all_courses(self):
        return self.__courses

class CourseRecordApplication:
    def __init__(self):
        self.__course_record = CourseRecord()

    def menu(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name    = input("course: ")
        grade   = int(input("grade: "))
        credits = int(input("credits: "))
        self.__course_record.add_course(name, grade, credits)

    def get_course_data(self):
        name = input("course: ")
        course = self.__course_record.get_course_data(name)
        if course is None:
            print("no entry for this course")
        else:
            print(course)

    def statistics(self):
        num_courses   = 0
        total_credits = 0
        total_grade   = 0

        courses = self.__course_record.all_courses()
        for course in courses.values():
            num_courses   += 1
            total_grade   += course.grade
            total_credits += course.credits

        stats_msg = f"{num_courses} completed courses, a total of {total_credits} credits"
        mean_msg  = f"mean {total_grade / num_courses:.1f}"
        print(stats_msg)
        print(mean_msg)
        self.grade_distribution()

    def grade_distribution(self):
        courses = self.__course_record.all_courses()
        grade_dist = [0] * 6
        for course in courses.values():
            grade_dist[course.grade] += 1
        print("grade distribution")
        for i in range(5, 0, -1):
            print(f"{i}: {"x" * grade_dist[i]}")

    def execute(self):
        self.menu()
        while True:
            print()

            try:
                command = int(input("command: "))
            except ValueError:
                print("Please enter an integer number")
                continue

            if command == 0:
                break
            elif command == 1:
                self.add_course()
            elif command == 2:
                self.get_course_data()
            elif command == 3:
                self.statistics()
            else:
                self.menu()

def main():
    CourseRecordApplication().execute()

main()

# if __name__ == "__main__":
#     course =  Course("ItP")
#     print(course)

# 1 add course
# 2 get course data
# 3 statistics
# 0 exit

# command: 1
# course: ItP
# grade: 3
# credits: 5

# command: 2
# course: ItP
# ItP (5 cr) grade 3

# command: 1
# course: ItP
# grade: 5
# credits: 5

# command: 2
# course: ItP
# ItP (5 cr) grade 5

# command: 1
# course: ItP
# grade: 1
# credits: 5

# command: 2
# course: ItP
# ItP (5 cr) grade 5

# command: 2
# course: Introduction to Java
# no entry for this course

# command: 1
# course: ACiP
# grade: 1
# credits: 10

# command: 1
# course: ItAI
# grade: 2
# credits: 5

# command: 1
# course: Algo101
# grade: 4
# credits: 1

# command: 1
# course: CompModels
# grade: 5
# credits: 8

# command: 3
# 5 completed courses, a total of 29 credits
# mean 3.4
# grade distribution
# 5: xx
# 4: x
# 3:
# 2: x
# 1: x

# command: 0
