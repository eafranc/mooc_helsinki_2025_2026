# Write your solution here
def hash_square(n):
    row = 1
    while (row <= n):
        print("#"*n)
        row += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)