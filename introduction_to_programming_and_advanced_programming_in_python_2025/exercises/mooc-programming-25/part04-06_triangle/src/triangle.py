# Copy here code of line function from previous exercise
def line(number, string):
    if (len(string) > 0):
        print(string[0]*number)
    else:
        print("*"*number)
def triangle(size):
    i = 1
    while (i <= size):
        line(i, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
