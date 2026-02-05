# Write your solution here
def write_file(filename: str, items : list):
    with open(filename, "w") as write_file:
        for item in items:
            write_file.write(item)

def filter_solutions():
    correct   = []
    incorrect = []
    with open("solutions.csv") as read_file:
        for line in read_file:
            [name, problem, result] = line.split(";")
            if "+" in problem:
                [num1, num2] = problem.split("+")
                if int(num1) + int(num2) == int(result):
                    correct.append(f"{name};{problem};{result}")
                else:
                    incorrect.append(f"{name};{problem};{result}")
            elif "-" in problem:
                [num1, num2] = problem.split("-")
                if int(num1) - int(num2) == int(result):
                    correct.append(f"{name};{problem};{result}")
                else:
                    incorrect.append(f"{name};{problem};{result}")

        write_file("correct.csv", correct)
        write_file("incorrect.csv", incorrect)

if __name__ == "__main__":
    filter_solutions()
# Arto;2+5;7
# Pekka;3-2;1
# Erkki;9+3;11
# Arto;8-3;4
# Pekka;5+5;10
# ...jne...
