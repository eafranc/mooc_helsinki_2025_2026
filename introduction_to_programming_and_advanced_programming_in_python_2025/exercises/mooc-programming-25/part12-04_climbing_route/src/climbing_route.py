class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:
def sort_by_length(items: list):
    def order_by_length(item: ClimbingRoute):
        return item.length

    return sorted(items, key=order_by_length, reverse=True)

def sort_by_difficulty(items: list):
    def order_by_difficulty(item: ClimbingRoute):
        return (item.grade, item.length) # tuples are sorted by their first element by default (the second element matters when there's a tie)

    return sorted(items, key=order_by_difficulty, reverse=True)

if __name__ == "__main__":
##########################################################################
    print("=" * 100)
    print("PART 1")

    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 11, "7A")
    r3 = ClimbingRoute("Synchro", 14, "8C+")
    r4 = ClimbingRoute("Small steps", 12, "6A+")

    routes = [r1, r2, r3, r4]

    for route in sort_by_length(routes):
        print(route)
# Edge, length 38 metres, grade 6A+
# Synchro, length 14 metres, grade 8C+
# Small steps, length 12 metres, grade 6A+
# Smooth operator, length 11 metres, grade 7A
##########################################################################
    print("=" * 100)
    print("PART 2")

    for route in sort_by_difficulty(routes):
        print(route)
# Synchro, length 14 metres, grade 8C+
# Smooth operator, length 11 metres, grade 7A
# Edge, length 38 metres, grade 6A+
# Small steps, length 12 metres, grade 6A+
##########################################################################
