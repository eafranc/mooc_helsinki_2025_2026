# Write your solution here
def greatest_number(a, b, c):
    x = a
    if b > x:
        x = b
    if c > x:
        x = c

    return x
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)