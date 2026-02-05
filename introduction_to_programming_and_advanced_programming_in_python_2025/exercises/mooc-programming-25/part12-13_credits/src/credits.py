from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"
# Write your solution
def sum_of_all_credits(attempts: list[CourseAttempt]):
    return reduce(lambda acc, item: acc + item.credits, attempts, 0)

def sum_of_passed_credits(attempts: list[CourseAttempt]):
    return reduce(lambda acc, item: acc + item.credits, filter(lambda ca: ca.grade >=1, attempts), 0)

def average(attempts: list[CourseAttempt]):
    passed_attempts = list(filter(lambda ca: ca.grade >= 1, attempts))
    return reduce(lambda acc, item: acc + item.grade / len(passed_attempts), passed_attempts , 0)

if __name__ == "__main__":
##################################################################################
    print("=" * 100)
    print("PART 1\n")

    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_all_credits([s1, s2, s3])
    print(credit_sum) # 20
##################################################################################
    print("=" * 100)
    print("PART 2\n")

    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_passed_credits([s1, s2, s3]) # 15
    print(credit_sum)
##################################################################################
    print("=" * 100)
    print("PART 2\n")

    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3]) # 4.0
    print(ag)

    print("=" * 100)
##################################################################################
