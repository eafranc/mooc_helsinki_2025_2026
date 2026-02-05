# Write your solution here
def print_persons(filename: str):
    import json
    with open(filename) as file:
        data = file.read()
        persons = json.loads(data)
        # print(persons)
    for person in persons:
        hobbies = ""
        i = 0
        for hobby in person["hobbies"]:
            hobbies += hobby
            if i < len(person["hobbies"]) - 1:
                hobbies += ", "
            i += 1
        print(f"{person["name"]} {person["age"]} years ({hobbies})")

if __name__ == "__main__":
    print_persons("file1.json")
# Peter Pythons 27 years (coding, knitting)
# Jean Javanese 24 years (coding, rock climbing, reading)
