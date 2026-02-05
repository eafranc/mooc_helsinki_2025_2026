# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people = []

    def add(self, person: Person):
        self.people.append(person)

    def is_empty(self):
        return len(self.people) == 0

    def print_contents(self):
        if len(self.people) > 0:
            combined_height = 0
            for person in self.people:
                combined_height += person.height
            print(f"There are {len(self.people)} persons in the room, and their combined height is {combined_height} cm")
            for person in self.people:
                print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if len(self.people) == 0:
            return None
        else:
            min_height      = self.people[0].height
            shortest_person = self.people[0]
            for person in self.people:
                if person.height < min_height:
                    min_height = person.height
                    shortest_person = person
            return shortest_person

    def remove_shortest(self):
        to_be_removed = self.shortest()
        if to_be_removed:
            self.people.remove(to_be_removed)
        return to_be_removed

if __name__ == "__main__":
#######################################################################
    print("=" * 30)
    print("PART 1")

    room = Room()
    print("Is the room empty?", room.is_empty()) # Is the room empty? True
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 155))
    print("Is the room empty?", room.is_empty()) # Is the room empty? False
    room.print_contents()
# There are 5 persons in the room, and their combined height is 838 cm
# Lea (183 cm)
# Kenya (172 cm)
# Ally (166 cm)
# Nina (162 cm)
# Dorothy (155 cm)
#######################################################################
    print("=" * 30)
    print("PART 2")

    room = Room()

    print("Is the room empty?", room.is_empty()) # Is the room empty? True
    print("Shortest:", room.shortest()) # Shortest: None

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))

    print()

    print("Is the room empty?", room.is_empty()) # Is the room empty? False
    print("Shortest:", room.shortest()) # Shortest: Nina

    print()

    room.print_contents()
# There are 4 persons in the room, and their combined height is 683 cm
# Lea (183 cm)
# Kenya (172 cm)
# Nina (162 cm)
# Ally (166 cm)
#######################################################################
    print("=" * 30)
    print("PART 3")

    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()
# There are 4 persons in the room, and their combined height is 683 cm
# Lea (183 cm)
# Kenya (172 cm)
# Nina (162 cm)
# Ally (166 cm)

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}") # Removed from room: Nina

    print()

    room.print_contents()
# There are 3 persons in the room, and their combined height is 521 cm
# Lea (183 cm)
# Kenya (172 cm)
# Ally (166 cm)
    print("=" * 30)
#######################################################################
