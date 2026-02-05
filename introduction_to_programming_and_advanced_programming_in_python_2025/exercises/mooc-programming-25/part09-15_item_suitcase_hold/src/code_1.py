# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

class Suitcase:
    def __init__(self, max_weight: int):
        if max_weight <= 0:
            raise ValueError("Maximum weight must not be less than zero")
        else:
            self.__max_weight = max_weight
        self.__items = []

    def __str__(self):
        total_weight = 0
        number_items = 0
        for item in self.__items:
            total_weight += item.weight()
            number_items += 1
        msg = f"{number_items} item"
        msg += "s" if len(self.__items) != 1 else ""
        msg += f" ({total_weight} kg)"
        return msg

    def add_item(self, new_item: Item):
        combined_weight = self.weight()
        if combined_weight + new_item.weight() <= self.__max_weight:
            self.__items.append(new_item)

    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        combined_weight = 0
        for item in self.__items:
            combined_weight += item.weight()
        return combined_weight

    def heaviest_item(self): # returns a reference to the heaviest object in the suitcase; if there's more than one, returns the first
        if len(self.__items) == 0:
            return None # if there's no objects inside the suitcase, returns None
        else:
            max_weight = 0
            for item in self.__items:
                if max_weight < item.weight():
                    max_weight = item.weight()
                    max_object = item
            return max_object

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []

    def __str__(self):
        suitcases_number = 0
        suitcases_weight = 0
        for suitcase in self.__suitcases:
            suitcases_weight += suitcase.weight()
            suitcases_number += 1
        msg = f"{suitcases_number} suitcase"
        msg += "s" if suitcases_number !=1 else ""
        msg += f", space for {self.__max_weight - suitcases_weight} kg"
        return msg

    def add_suitcase(self, new_suitcase: Suitcase):
        suitcases_combined_weight = 0
        for suitcase in self.__suitcases:
            suitcases_combined_weight = suitcase.weight()
        if suitcases_combined_weight + new_suitcase.weight() <= self.__max_weight:
            self.__suitcases.append(new_suitcase)

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

if __name__ == "__main__":
#######################################################################################################
    print("=" * 50)
    print("PART 1")

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)

    print("Name of the book:", book.name()) # Name of the book: ABC Book
    print("Weight of the book:", book.weight()) # Weight of the book: 2

    print("Book:", book) # Book: ABC Book (2 kg)
    print("Phone:", phone) # Phone: Nokia 3210 (1 kg)
#######################################################################################################
    print("=" * 50)
    print("PART 2 & 3")

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(5)
    print(suitcase) # 0 items (0 kg)

    suitcase.add_item(book)
    print(suitcase) # 1 items (2 kg)

    suitcase.add_item(phone)
    print(suitcase) # 2 items (3 kg)

    suitcase.add_item(brick)
    print(suitcase) # 2 items (3 kg)
#######################################################################################################
    print("=" * 50)
    print("PART 4")

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    print("The suitcase contains the following items:")
    suitcase.print_items()
# The suitcase contains the following items:
# ABC Book (2 kg)
# Nokia 3210 (1 kg)
# Brick (4 kg)
    combined_weight = suitcase.weight()
    print(f"Combined weight: {combined_weight} kg") # Combined weight: 7 kg
#######################################################################################################
    print("=" * 50)
    print("PART 5")

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    heaviest = suitcase.heaviest_item()
    print(f"The heaviest item: {heaviest}") # The heaviest item: Brick (4 kg)
#######################################################################################################
    print("=" * 50)
    print("PART 6")

    cargo_hold = CargoHold(1000)
    print(cargo_hold) # 0 suitcases, space for 1000 kg

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold.add_suitcase(adas_suitcase)
    print(cargo_hold) # 1 suitcase, space for 997 kg

    cargo_hold.add_suitcase(peters_suitcase)
    print(cargo_hold) # 2 suitcases, space for 993 kg
#######################################################################################################
    print("=" * 50)
    print("PART 7")

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
# The suitcases in the cargo hold contain the following items:
# ABC Book (2 kg)
# Nokia 3210 (1 kg)
# Brick (4 kg)
    print("=" * 50)
#######################################################################################################
