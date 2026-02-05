# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        largest_number = 0
        for line in new_file:
            if int(line) > largest_number:
                largest_number = int(line)
        return largest_number

if __name__ == "__main__":
    largest_num = largest()
    print(largest_num)
