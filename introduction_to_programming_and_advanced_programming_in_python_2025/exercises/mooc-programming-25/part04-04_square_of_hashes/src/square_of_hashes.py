# Copy here code of line function from previous exercise
def line(number, string):
    if (len(string) > 0):
        print(string[0]*number)
    else:
        print("*"*number)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    i = 0
    while (i < size):
        line(size, "#")
        i +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
