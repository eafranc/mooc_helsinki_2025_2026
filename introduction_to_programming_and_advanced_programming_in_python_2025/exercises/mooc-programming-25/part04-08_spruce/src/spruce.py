# Write your solution here
def spruce(size):
    print("a spruce!")
    i = 0
    while (i < size):
        row = " "*(size - i -1) + "*"*(2*i + 1)
        print(row)
        i +=1
    print(" "*(i-1) + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
    print("--------------------------------")
    spruce(3)