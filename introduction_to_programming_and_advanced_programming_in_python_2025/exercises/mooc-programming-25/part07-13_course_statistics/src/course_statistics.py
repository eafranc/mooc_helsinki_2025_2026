# Write your solution here
def retrieve_all():
    import urllib.request
    import json

    my_request        = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    my_request_data   = my_request.read()
    json_data_courses = json.loads(my_request_data)

    courses_tuples = []
    for course in json_data_courses:
        if course["enabled"]:
            courses_tuples.append((course["fullName"], course["name"], course["year"], sum(course["exercises"])))
    return courses_tuples

def retrieve_course(course_name: str):
    import urllib.request
    import json

    course_url     = "https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats".replace("****", course_name)
    course_request = urllib.request.urlopen(course_url)
    course_data    = course_request.read()
    json_course    = json.loads(course_data)

    weeks     = 0
    students  = 0
    hours     = 0
    exercises = 0
    for week in json_course:
        weeks     += 1
        if students < int(json_course[week]["students"]):
            students = int(json_course[week]["students"])
        hours     += int(json_course[week]["hour_total"])
        exercises += int(json_course[week]["exercise_total"])

    hours_average = hours // students
    exercises_average = exercises // students

    course = {
    "weeks"            : weeks,
    "students"         : students,
    "hours"            : hours,
    "hours_average"    : hours_average,
    "exercises"        : exercises,
    "exercises_average": exercises_average
    }
    return course

if __name__ == "__main__":
    courses = retrieve_all()
    for course in courses:
        print(course)
# [
#     ('Full Stack Open 2020', 'ofs2019', 2020, 201),
#     ('DevOps with Docker 2019', 'docker2019', 2019, 36),
#     ('DevOps with Docker 2020', 'docker2020', 2020, 36),
#     ('Beta DevOps with Kubernetes', 'beta-dwk-20', 2020, 28)
# ]
    course_dictionary = retrieve_course("docker2019")
    print(course_dictionary)
# {
#     'weeks': 4,
#     'students': 220,
#     'hours': 5966,
#     'hours_average': 27,
#     'exercises': 4988,
#     'exercises_average': 22
# }
