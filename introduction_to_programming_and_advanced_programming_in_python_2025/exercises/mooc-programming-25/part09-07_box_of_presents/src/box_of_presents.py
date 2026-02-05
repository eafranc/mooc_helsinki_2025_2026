# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self, name: str, weight: int):
        self.name   = name
        self.weight = weight

    def __str__(self):
        return f"Present: {self.name} ({self.weight} kg)"

class Box:
    def __init__(self):
        self.presents = []
        self.weight   = 0

    def __str__(self):
        text1 =  f"What's in the box: \n"
        presents_name_list = []
        for present in self.presents:
            presents_name_list.append(present.name)
        text2 = f"{", ".join(presents_name_list)}"
        return text1 + text2

    def add_present(self, present: Present):
        self.presents.append(present)
        self.weight += present.weight

    def total_weight(self):
        return self.weight

if __name__ == "__main__":
    print("=" * 30)
    print("PART 1")
######################################################
    book = Present("ABC Book", 2)

    print("The name of the present:", book.name) # The name of the present: ABC Book
    print("The weight of the present:", book.weight) # The weight of the present: 2
    print("Present:", book) # Present: ABC Book (2 kg)

    print("=" * 30)
    print("PART 2")
######################################################
    book = Present("ABC Book", 2)

    box = Box()
    box.add_present(book)
    print(box.total_weight()) # 2

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight()) # 3

    print(box)

    print("=" * 30)
######################################################
