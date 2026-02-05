# Write your solution here
def chessboard(length):
    row = 1
    while (row <= length):
        column = 1
        line = ""
        while (column <= length):
            if (not (column + row)%2):
                line += "1"
            else:
                line += "0"
            column +=1
        row +=1
        print(line)    
   
# Testing the function
if __name__ == "__main__":
    chessboard(3)
    print("****")
    chessboard(8)
