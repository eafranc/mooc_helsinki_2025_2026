def min_count(product_count, box_size):
    """
    The idea: if you add the maximum remainder (which is d - 1, in which d is the divisor)
    to the quotient, then the even division [q + (d -1)] // d will add 1 to the result of 
    the division q // d if the division is not even and add 0 if the division is even.

    This solves the problem, for example, of figuring out how many bottle containers 
    I will need if each container can keep 3 bottles and I have 10 bottles in total:
    [(10 + (3 - 1)] // 3 = 4, i.e, 3 containers full with 3 bottles each and 1 container
    with only 1 bottle.
    """
    return (product_count + (box_size - 1)) // box_size


if __name__ == "__main__":
    print(min_count(10, 3)) # 4
    print(min_count(10, 4)) # 3
    print(min_count(100, 1)) # 100
    print(min_count(100, 100)) # 1
    print(min_count(100, 99)) # 2
    print(min_count(5, 5)) # 1
    print(min_count(5, 6)) # 1
