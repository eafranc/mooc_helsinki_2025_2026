# Write your solution here
def oldest_person(people: list):
    [oldest_name, oldest_year] = people[0]
    for name, year in people:
        if year < oldest_year:
            oldest_year = year
            oldest_name = name
    return oldest_name

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
    print(oldest_person(people)) # Mary