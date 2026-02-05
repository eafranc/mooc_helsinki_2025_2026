# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        fruits = {}
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruit = parts[0]
            price = float(parts[1])
            fruits[fruit] = price
    return fruits

if __name__ == "__main__":
    fruits_dict = read_fruits()
    print(fruits_dict)
    for key, value in fruits_dict.items():
        print(f"{key}: {value}")