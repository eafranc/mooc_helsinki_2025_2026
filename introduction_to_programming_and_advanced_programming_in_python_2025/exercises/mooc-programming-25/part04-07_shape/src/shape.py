# Copy here code of line function from previous exercise and use it in your solution
def line(number, string):
    if (len(string) > 0):
        print(string[0]*number)
    else:
        print("*"*number)

# Function shape
def shape(tri_size, tri_char, rect_height, rect_char):
    i = 1
    while (i <= tri_size):
        line(i, tri_char)
        i +=1
    i = 1
    while(i <= rect_height):
        line(tri_size, rect_char)
        i +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")