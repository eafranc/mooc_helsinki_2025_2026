# Write your solution here
def factorials(n: int):
    factorial = {}
    for i in range(1, n + 1):
        if i in [1]: # Actually, it could be [0, 1], but this exercise is not interested in 0! = 1
            factorial[i] = 1
        else:
            factorial[i] = i*factorial[i-1]
    return factorial

if __name__ == "__main__":
    k = factorials(5)
    print(k[1]) # 1
    print(k[3]) # 6
    print(k[5]) # 120
