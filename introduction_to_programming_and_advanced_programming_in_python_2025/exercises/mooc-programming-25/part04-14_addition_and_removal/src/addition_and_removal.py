# Write your solution here
list_values = []

while True:
    msg = f"The list is now {list_values}"
    print(msg)    
    option = input("a(d)d, (r)emove or e(x)it:")

    if option == "d":
        if len(list_values) == 0:
            list_values.append(1)
            continue           
        else:
            list_values.append(list_values[-1] + 1)
            continue          
    elif option == "r":
        list_values.pop(-1)
        continue        
    elif option == "x":
        print("Bye!")
        break