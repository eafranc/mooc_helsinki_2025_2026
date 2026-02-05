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

# def create_rules():
#     rules = []

#     # ============================================
#     # FASE 1: VERIFICAR PARIDADE
#     # ============================================

#     # Estado 1: inicial
#     rules.append(("L", 1, "L", 2, "RIGHT"))
    
#     # Estado 2: posição PAR | Estado 3: posição ÍMPAR
#     for s in ["0", "1"]:
#         rules.append((s, 2, s, 3, "RIGHT"))
#         rules.append((s, 3, s, 2, "RIGHT"))

#     rules.append(("R", 2, "R", 4, "LEFT"))     # par → fase 2
#     rules.append(("R", 3, "R", 3, "REJECT"))   # ímpar → rejeita

#     # ============================================
#     # FASE 2: ENCONTRAR O MEIO (zig-zag)
#     # Metade esquerda: 0→A, 1→B
#     # Metade direita: 0→C, 1→D
#     # ============================================

#     # Estado 4: indo ESQUERDA, marcando metade DIREITA
#     rules.append(("C", 4, "C", 4, "LEFT"))     # pula já marcado
#     rules.append(("D", 4, "D", 4, "LEFT"))     # pula já marcado
#     rules.append(("0", 4, "C", 5, "LEFT"))     # marca 0→C
#     rules.append(("1", 4, "D", 5, "LEFT"))     # marca 1→D
#     rules.append(("A", 4, "A", 8, "LEFT"))     # achou A → meio encontrado!
#     rules.append(("B", 4, "B", 8, "LEFT"))     # achou B → meio encontrado!
#     rules.append(("L", 4, "L", 6, "RIGHT"))    # string curta, muda direção

#     # Estado 5: voltando para esquerda após marcar direita
#     rules.append(("0", 5, "0", 5, "LEFT"))
#     rules.append(("1", 5, "1", 5, "LEFT"))
#     rules.append(("A", 5, "A", 6, "RIGHT"))    # chegou no limite → muda direção
#     rules.append(("B", 5, "B", 6, "RIGHT"))
#     rules.append(("L", 5, "L", 6, "RIGHT"))

#     # Estado 6: indo DIREITA, marcando metade ESQUERDA
#     rules.append(("A", 6, "A", 6, "RIGHT"))    # pula já marcado
#     rules.append(("B", 6, "B", 6, "RIGHT"))    # pula já marcado
#     rules.append(("0", 6, "A", 7, "RIGHT"))    # marca 0→A
#     rules.append(("1", 6, "B", 7, "RIGHT"))    # marca 1→B
#     rules.append(("C", 6, "C", 8, "LEFT"))     # achou C → meio encontrado!
#     rules.append(("D", 6, "D", 8, "LEFT"))     # achou D → meio encontrado!
#     rules.append(("R", 6, "R", 6, "ACCEPT"))   # string vazia

#     # Estado 7: voltando para direita após marcar esquerda
#     rules.append(("0", 7, "0", 7, "RIGHT"))
#     rules.append(("1", 7, "1", 7, "RIGHT"))
#     rules.append(("C", 7, "C", 4, "LEFT"))     # chegou no limite → muda direção
#     rules.append(("D", 7, "D", 4, "LEFT"))
#     rules.append(("R", 7, "R", 4, "LEFT"))

#     # Estado 8: meio encontrado, volta para L
#     for s in ["A", "B", "C", "D"]:
#         rules.append((s, 8, s, 8, "LEFT"))
#     rules.append(("L", 8, "L", 9, "RIGHT"))

#     # ============================================
#     # FASE 3: COMPARAR METADES
#     # Após comparar: A→E, B→F, C→G, D→H
#     # ============================================

#     # Estado 9: procura próximo A ou B
#     rules.append(("E", 9, "E", 9, "RIGHT"))    # pula já comparado
#     rules.append(("F", 9, "F", 9, "RIGHT"))    # pula já comparado
#     rules.append(("A", 9, "E", 10, "RIGHT"))   # achou A (era 0) → busca C
#     rules.append(("B", 9, "F", 11, "RIGHT"))   # achou B (era 1) → busca D
#     for s in ["C", "D", "G", "H"]:
#         rules.append((s, 9, s, 9, "ACCEPT"))   # acabou comparação

#     # Estado 10: tinha 0 na esquerda, procura C
#     for s in ["E", "F", "G", "H", "A", "B"]:
#         rules.append((s, 10, s, 10, "RIGHT"))
#     rules.append(("C", 10, "G", 12, "LEFT"))   # C (era 0) → match!
#     rules.append(("D", 10, "D", 10, "REJECT")) # D (era 1) → mismatch!

#     # Estado 11: tinha 1 na esquerda, procura D
#     for s in ["E", "F", "G", "H", "A", "B"]:
#         rules.append((s, 11, s, 11, "RIGHT"))
#     rules.append(("D", 11, "H", 12, "LEFT"))   # D (era 1) → match!
#     rules.append(("C", 11, "C", 11, "REJECT")) # C (era 0) → mismatch!

#     # Estado 12: match, volta para L
#     for s in ["E", "F", "G", "H", "A", "B", "C", "D"]:
#         rules.append((s, 12, s, 12, "LEFT"))
#     rules.append(("L", 12, "L", 9, "RIGHT"))   # volta para estado 9

#     return rules

def create_rules():
    rules = []
    #####################################################################################################################################
    ### PHASE 1 - Finding all the 0s and 1s in the whole string
    #  - Mark them as 0->A and 1->B on the left and 0->C and 1->D on the right
    #####################################################################################################################################
    # STATE 1 - Goes from L and tries to find the first 0/1 to change to A/B (goes to STATE 2);
    # if it doesn't find 0/1, turns to STATE 5 when finds the first C/D (meaning that there are no 0/1 left in the whole string)
    rules.append(("L", 1, "L", 1, "RIGHT"))
    rules.append(("0", 1, "A", 2, "RIGHT"))
    rules.append(("1", 1, "B", 2, "RIGHT"))
    rules.append(("A", 1, "A", 1, "RIGHT"))
    rules.append(("B", 1, "B", 1, "RIGHT"))
    rules.append(("C", 1, "C", 5, "LEFT"))
    rules.append(("D", 1, "D", 5, "LEFT"))
    # STATE 2 - After finding 0/1 on the left, goes towards R (goes to STATE 3) and ignores every symbol
    rules.append(("0", 2, "0", 2, "RIGHT"))
    rules.append(("1", 2, "1", 2, "RIGHT"))
    rules.append(("C", 2, "C", 2, "RIGHT"))
    rules.append(("D", 2, "D", 2, "RIGHT"))
    rules.append(("R", 2, "R", 3, "LEFT"))
    # STATE 3 - Goes from R and tries to find the nearest 0/1 to change to C/D (goes to STATE 4)
    rules.append(("0", 3, "C", 4, "LEFT"))
    rules.append(("1", 3, "D", 4, "LEFT"))
    rules.append(("C", 3, "C", 3, "LEFT"))
    rules.append(("D", 3, "D", 3, "LEFT"))
    # STATE 4 - After finding 0/1 on STATE 3, goes towards L and ignores every symbol;
    # when in L, changes to STATE 1 and tries again to find the nearest 0/1 on the left
    rules.append(("0", 4, "0", 4, "LEFT"))
    rules.append(("1", 4, "1", 4, "LEFT"))
    rules.append(("A", 4, "A", 4, "LEFT"))
    rules.append(("B", 4, "B", 4, "LEFT"))
    rules.append(("L", 4, "L", 1, "RIGHT"))
    #####################################################################################################################################
    ### PHASE 2 - Checking A and B on the left and comparing with the corresponding C and D on the right
    #  - Always picks the leftmost A or B and compares to the leftmost C or D, marks checked positions (A, B, C and D) with X
    #####################################################################################################################################
    # STATE 5 - When in STATE 1, if there are no 0/1s left, goes to STATE 5 when finds first C/D, then changes direction towards L
    # goes to STATE 6 when it gets to L)
    rules.append(("A", 5, "A", 5, "LEFT"))
    rules.append(("B", 5, "B", 5, "LEFT"))
    rules.append(("X", 5, "X", 5, "LEFT"))
    rules.append(("L", 5, "L", 6, "RIGHT"))
    # STATE 6 - Going from L, finds first A and changes it to X (goes to STATE 7) or finds first B and changes it to X (goes to STATE 8)
    rules.append(("A", 6, "X", 7, "RIGHT"))
    rules.append(("B", 6, "X", 8, "RIGHT"))
    rules.append(("X", 6, "X", 6, "RIGHT"))
    rules.append(("R", 6, "R", 6, "ACCEPT"))
    # STATE 7 - After checking first A on the left (marked as X), finds the corresponding nearest C,
    # then changes to STATE 5 and goes towards L; skips marked symbols (X), A and B
    rules.append(("C", 7, "X", 5, "LEFT"))
    rules.append(("X", 7, "X", 7, "RIGHT"))
    rules.append(("A", 7, "A", 7, "RIGHT"))
    rules.append(("B", 7, "B", 7, "RIGHT"))
    # STATE 8 - After checking first B on the left (marked as X), finds the corresponding nearest D,
    # then changes to STATE 5 and goes towards L; skips marked symbols (X), A and B
    rules.append(("D", 8, "X", 5, "LEFT"))
    rules.append(("X", 8, "X", 8, "RIGHT"))
    rules.append(("A", 8, "A", 8, "RIGHT"))
    rules.append(("B", 8, "B", 8, "RIGHT"))

    return rules


if __name__ == "__main__":
    rules = create_rules()

    print(calculate("00", rules)) # True
    print(calculate("001001", rules)) # True
    print(calculate("10111011", rules)) # True
    print(calculate("01", rules)) # False
    print(calculate("00100", rules)) # False
    print(calculate("10111101", rules)) # False
