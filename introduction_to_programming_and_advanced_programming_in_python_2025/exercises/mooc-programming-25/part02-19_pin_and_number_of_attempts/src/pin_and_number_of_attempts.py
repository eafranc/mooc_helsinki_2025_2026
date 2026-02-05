# Write your solution here
attempts = 0
msg_wrong       = "Wrong"
msg_right_1_att = "Correct! It only took you one single attempt!"
msg_right_n_att = "Correct! It took you "
while True:
    pin=(input("PIN:"))
    attempts+=1
    if (pin == "4321"):
        break
    else:
        msg = msg_wrong
        print(msg)
if (attempts == 1):
    msg = msg_right_1_att
else:
    msg_right_n_att += f"{attempts} attempts"
    msg = msg_right_n_att
print(msg)
        