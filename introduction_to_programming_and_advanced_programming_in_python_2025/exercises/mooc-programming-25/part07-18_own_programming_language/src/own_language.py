# Write your solution here
def run(program : list):
    from string import ascii_uppercase

    variables    = {}
    print_output = []
    jump_labels  = {}

    for ch in ascii_uppercase: # Initializing all 26 variables (A, B, C, ..., Z) with 0
        variables[ch] = 0

    # PRE-PROCESS ALL THE LABELS BEFORE EXECUTING THE LINES!!!
    for i, line in enumerate(program):
        if line.endswith(":"): # [location]:: names a line of code, so it can be jumped to from elsewhere
            label_name = line[:-1] # Removes the ":"
            jump_labels[label_name] = i

    line_number = 0
    while (line_number < len(program)):

        line = program[line_number]

        if line.startswith("PRINT"): # PRINT [value]: prints the value
            [_, value] = line.split(" ")
            print_output.append(int(value)) if value.isdigit() else print_output.append(variables[value])

        elif line.startswith("MOV"): # MOV [variable] [value]: assigns the value to the variable
            [_, variable, value] = line.split(" ")
            variables[variable] = int(value) if value.isdigit() else variables[value]

        elif line.startswith("ADD"): # ADD [variable] [value]: adds the value to the variable
            [_, variable, value] = line.split(" ")
            variables[variable] += int(value) if value.isdigit() else variables[value]

        elif line.startswith("SUB"): # SUB [variable] [value]: subtracts the value from the variable
            [_, variable, value] = line.split(" ")
            variables[variable] -= int(value) if value.isdigit() else variables[value]

        elif line.startswith("MUL"): # MUL [variable] [value]: multiplies the variable by the value
            [_, variable, value] = line.split(" ")
            variables[variable] *= int(value) if value.isdigit() else variables[value]

        elif line.startswith("JUMP"): # JUMP [location]: jumps to the location specified
            [_, location] = line.split(" ")
            line_number = jump_labels[location]
            continue

        elif line.startswith("IF"): # IF [condition] JUMP [location]: if the condition is true, jump to the location specified
            [_, value1, comparison, value2, _, location] = line.split(" ") # [condition] is equivalent to [value] [comparison] [value]
            if comparison == "<":
                condition = (int(value1) if value1.isdigit() else variables[value1]) < (int(value2) if value2.isdigit() else variables[value2])
            elif comparison == "<=":
                condition = (int(value1) if value1.isdigit() else variables[value1]) <= (int(value2) if value2.isdigit() else variables[value2])
            elif comparison == ">":
                condition = (int(value1) if value1.isdigit() else variables[value1]) > (int(value2) if value2.isdigit() else variables[value2])
            elif comparison == ">=":
                condition = (int(value1) if value1.isdigit() else variables[value1]) >= (int(value2) if value2.isdigit() else variables[value2])
            elif comparison == "==":
                condition = (int(value1) if value1.isdigit() else variables[value1]) == (int(value2) if value2.isdigit() else variables[value2])
            elif comparison == "!=":
                condition = (int(value1) if value1.isdigit() else variables[value1]) != (int(value2) if value2.isdigit() else variables[value2])

            if condition == True:
                line_number = jump_labels[location]
                continue

        elif line == "END":
            break

        line_number += 1 # increment line_number
    return print_output

if __name__ == "__main__":
    program_teste = []
    program_teste.append("PRINT 5")
    program_teste.append("MOV A 10")
    program_teste.append("PRINT A")
    program_teste.append("END")
    result = run(program_teste)
    print(result)  # Must output: [5, 10]

    program_bug = []
    program_bug.append("MOV A 10")
    program_bug.append("MOV B 5")
    program_bug.append("ADD A B")
    program_bug.append("PRINT A")
    program_bug.append("END")
    result = run(program_bug)
    print(result) # A should turn to 15

# # EXAMPLE 1
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result) # [1, 2, 3]

# EXAMPLE 2
    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result) # [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

# EXAMPLE 3 - FACTORIAL
    program3 = []
    program3.append("MOV A 1")
    program3.append("MOV B 1")
    program3.append("begin:")
    program3.append("PRINT A")
    program3.append("ADD B 1")
    program3.append("MUL A B")
    program3.append("IF B <= 10 JUMP begin")
    program3.append("END")
    result = run(program3)
    print(result) # [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

# EXAMPLE 4 - PRIME NUMBERS
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
