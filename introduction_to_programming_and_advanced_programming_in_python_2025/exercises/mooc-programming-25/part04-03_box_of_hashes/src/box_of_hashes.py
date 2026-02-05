# Copy here code of line function from previous exercise
def line(number, string):
    if (len(string) > 0):
        print(string[0]*number)
    else:
        print("*"*number)

def box_of_hashes(height):
    # You should call function line here with proper parameters
    i = 0
    while (i < height):
        line(10, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(2)
    print()
    box_of_hashes(0)

