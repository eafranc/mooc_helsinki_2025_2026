def calculate(input, rules):
    # 1. Creates a list using the string and L and R on its ends
    input = list("L" + input + "R")

    # 2. Initial state
    state = 1
    position = 0

    # 3. Simulation loop (1000 steps max)
    for _ in range(1000):
        symbol = input[position]

        if len(rules) == 0: # if there are no rules: return False
            return False

        # 4. Finds rule that combines (symbol, state)
        found_rule = None
        for rule in rules:
            if rule[0] == symbol and rule[1] == state:
                found_rule = rule
                break

        if found_rule is None: # each combination of a symbol and a state activates at most one rule (a tuple with 5 elements)
            return False

        _, _, new_symbol, new_state, action = found_rule # destructure the rule found for legibility

        # 5. Applies the rule
        input[position] = new_symbol # - Change symbol
        state = new_state # - Change state

        # 6. Executes action (LEFT, RIGHT, ACCEPT, REJECT)
        if action == "RIGHT":
            position += 1
        elif action == "LEFT":
            position -= 1
        elif action == "ACCEPT":
            return True
        elif action == "REJECT":
            return False

        if position < 0 or position >= len(input): # if gets out of the string: return False
            return False

    # 7. If it gets here, it got over 1000 steps in the loop
    return False

if __name__ == "__main__":
    rules = []

    rules.append(("L", 1, "L", 2, "RIGHT"))
    rules.append(("L", 3, "L", 2, "RIGHT"))

    rules.append(("0", 2, "X", 4, "RIGHT"))
    rules.append(("1", 4, "X", 5, "RIGHT"))
    rules.append(("1", 2, "X", 6, "RIGHT"))
    rules.append(("0", 6, "X", 7, "RIGHT"))

    rules.append(("0", 4, "0", 4, "RIGHT"))
    rules.append(("0", 5, "0", 5, "RIGHT"))
    rules.append(("0", 7, "0", 7, "RIGHT"))
    rules.append(("1", 6, "1", 6, "RIGHT"))
    rules.append(("1", 5, "1", 5, "RIGHT"))
    rules.append(("1", 7, "1", 7, "RIGHT"))

    rules.append(("X", 2, "X", 2, "RIGHT"))
    rules.append(("X", 4, "X", 4, "RIGHT"))
    rules.append(("X", 5, "X", 5, "RIGHT"))
    rules.append(("X", 6, "X", 6, "RIGHT"))
    rules.append(("X", 7, "X", 7, "RIGHT"))

    rules.append(("R", 2, "R", 2, "ACCEPT"))
    rules.append(("R", 4, "R", 4, "REJECT"))
    rules.append(("R", 6, "R", 6, "REJECT"))

    rules.append(("R", 5, "R", 3, "LEFT"))
    rules.append(("R", 7, "R", 3, "LEFT"))
    rules.append(("0", 3, "0", 3, "LEFT"))
    rules.append(("1", 3, "1", 3, "LEFT"))
    rules.append(("X", 3, "X", 3, "LEFT"))

    print(calculate("0", rules)) # False
    print(calculate("00", rules)) # False
    print(calculate("01", rules)) # True
    print(calculate("0110", rules)) # True
    print(calculate("0101", rules)) # True
    print(calculate("1000", rules)) # False
    print(calculate("00110101", rules)) # True
    print(calculate("00111101", rules)) # False
