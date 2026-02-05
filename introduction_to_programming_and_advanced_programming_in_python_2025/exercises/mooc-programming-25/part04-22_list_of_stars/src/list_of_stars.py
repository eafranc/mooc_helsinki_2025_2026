# Write your solution here
def list_of_stars(nums: list):
    for num in nums:
        print("*" * num)

if __name__ == "__main__":
    list_of_stars([1, 2, 3, 4])
    print("\n================\n")
    list_of_stars([5, 3, 2, 4, 1, 0])