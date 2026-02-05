# Write your solution here:
class Person:
    def __init__(self, name: str):
        self.__name = name
        self.__numbers = []
        self.__address = None

    def __repr__(self):
        return f"Person('{self.__name}')"

    def __str__(self):
        number_str = ", ".join(self.__numbers) if self.__numbers else "none"
        address_str = self.__address if self.__address else "unknown"
        return f"name: {self.__name}, numbers: {number_str}, address: {address_str}"

    def name(self):
        return self.__name

    def numbers(self):
        return self.__numbers

    def address(self):
        return self.__address

    def add_number(self, number: str):
        self.__numbers.append(number)

    def add_address(self, address: str):
        self.__address = address

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")

        person = self.__phonebook.get_entry(name)

        if person is None:
            print("number unknown")
            print("address unknown")
            return

        numbers = person.numbers()
        if numbers:
            for number in numbers:
                print(number)
        else:
            print("number unknown")

        address = person.address()
        if address:
            print(address)
        else:
            print("address unknown")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()

def main():
    # when testing, no code should be outside application except the following:
    application = PhoneBookApplication()
    application.execute()

main()

if __name__ == "__main__":
#################################################################################
    print("=" * 50)
    print("PART 1")

    person = Person("Eric")
    print(person.name()) # Eric
    print(person.numbers()) # []
    print(person.address()) # None
    person.add_number("040-123456")
    person.add_address("Mannerheimintie 10 Helsinki")
    print(person.numbers()) # ['040-123456']
    print(person.address()) # Mannerheimintie 10 Helsink
#################################################################################
    print("=" * 50)
    print("PART 2")

    phonebook = PhoneBook()
    phonebook.add_number("Eric", "02-123456")
    print(phonebook.get_entry("Eric"))
    print(phonebook.get_entry("Emily"))
    print(phonebook.all_entries())
#################################################################################
    print("=" * 50)
    print("PART 3")

# commands:
# 0 exit
# 1 add number
# 2 search
# 3 add address

# command: 1
# name: Eric
# number: 02-123456

# command: 3
# name: Emily
# address: Viherlaaksontie 7, Espoo

# command: 2
# name: Eric
# 02-123456
# address unknown

# command: 2
# name: Emily
# number unknown
# Viherlaaksontie 7, Espoo

# command: 3
# name: Eric
# address: Linnankatu 75, Turku

# command: 2
# name: Eric
# 02-123456
# Linnankatu 75, Turku

# command: 2
# name: Wilhelm
# address unknown
# number unknown

# command: 0

    print("=" * 50)
#################################################################################
