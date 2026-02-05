# Write your solution here
def read_input(prompt: str, low: int, high: int):
    while True:
        try:
            number = int(input(prompt))
            if low <= number <= high:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {low} and {high}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)

# Please type in a number: seven
# You must type in an integer between 5 and 10
# Please type in a number: -3
# You must type in an integer between 5 and 10
# Please type in a number: 8
# You typed in: 8
