# Write your solution here
pw = input("Password:")
while True:
    rep_pw = input("Repeat password:")
    if rep_pw == pw:
        break
    else:
        print("They do not match!")
print("User account created!")