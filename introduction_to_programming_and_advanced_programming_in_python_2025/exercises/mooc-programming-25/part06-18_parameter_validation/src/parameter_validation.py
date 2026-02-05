# Write your solution here
def new_person(name: str, age: int):
    if name == "":
        raise ValueError("name is an empty string")
    if len(name.split(" ")) < 2:
        raise ValueError("name contains less than two words")
    if len(name) > 40:
        raise ValueError("name is longer than 40 characters")
    if age < 0:
        raise ValueError("age is a negative number")
    if age > 150:
        raise ValueError("age is greater than 150")

    return (name, age)
# if __name__ == "__main__":


# name is an empty string
# name contains less than two words
# name is longer than 40 characters
# age is a negative number
# age is greater than 150
