# Write your solution here
word = input("Word:")

if(len(word)%2 == 0):
    offset = 0
else:
    offset = 1

adjusted_word ="*"+" "*int(14-len(word)/2)+word+" "*int(14+offset-len(word)/2)+"*"
# Frame:
print("*" * 30)
print(adjusted_word)
print("*" * 30)