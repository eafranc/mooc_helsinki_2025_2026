# Write your solution here
def store_personal_data(person: tuple):
    (name, age, height) = person
    with  open("people.csv", "a") as write_file:
        line = f"{name};{age};{height}\n"
        write_file.write(line)

if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5)) # Paul Paulson;37;175.5
    store_personal_data(("Mia Khalifa", 29, 156.0)) # Mia Khalifa;29;156.0
