# Write your solution here
def get_dictionary():
    dictionary = {}
    with open("dictionary.txt") as read_dictionary:
        for line in read_dictionary:
            line = line.strip()
            parts = line.split("-")
            finnish = parts[0]
            english = parts[1]
            dictionary[english] = finnish
    return dictionary

def write_dictionary(english: str, finnish: str):
    with open("dictionary.txt", "a") as write_dictionary:
        write_dictionary.write(f"{finnish} - {english}\n")
    print("Dictionary entry added")

def evaluate_dictionary_entry(english: str):
    dictionary = get_dictionary()
    english_flag = True
    for english_key in dictionary:
        if english_key == english:
            english_flag = False
    return english_flag

def search_in_dictionary(search_term: str):
    dictionary = get_dictionary()
    not_found_flag = True
    for english_word in dictionary:
        if search_term in english_word or search_term in dictionary[english_word]:
            not_found_flag = False
            print (f"{dictionary[english_word]}-{english_word}")
    if not_found_flag == True:
        print(f"Search term {search_term} not found in the dictionary")

def display_dictionary():
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        function = int(input("Function: "))

        if function == 1:
            finnish = input("The word in Finnish: ")
            english = input("The word in English: ")
            if evaluate_dictionary_entry(english) == True:
                write_dictionary(english, finnish)
            else:
                print("This entry already exists in the dictionary")

        elif function == 2:
            search_term = input("Search term: ")
            search_in_dictionary(search_term)

        elif function == 3:
            print("Bye!")
            break

def main():
    display_dictionary()

main()

# 1 - Add word, 2 - Search, 3 - Quit
# Function: 1
# The word in Finnish: auto
# The word in English: car
# Dictionary entry added
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 1
# The word in Finnish: roska
# The word in English: garbage
# Dictionary entry added
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 1
# The word in Finnish: laukku
# The word in English: bag
# Dictionary entry added
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 2
# Search term: bag
# roska - garbage
# laukku - bag
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 2
# Search term: car
# auto - car
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 2
# Search term: laukku
# laukku - bag
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 3
# Bye!
