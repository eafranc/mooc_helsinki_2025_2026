# Write your solution here
def squared(string, n):
    row = 0
    while (row < n):
        line = ""
        index = 0
        while (index < n):
            line += string[((index + row*n)%(len(string)))]
            index += 1
        row +=1
        print(line)

# Test
if __name__ == "__main__":
    squared("ab", 3)
    print("-----------")
    squared("aybabtu", 5)