# Write your solution here
if True:
    name     = input("Whom should I sign this to: ")
    filename = input("Where shall I save it: ")
else:
    name     = "Ada"
    filename = "inscribed.txt"

with open(filename, "w") as file:
    file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

# Whom should I sign this to: Ada
# Where shall I save it: inscribed.txt

# Hi Ada, we hope you enjoy learning Python with us! Best, Mooc.fi Team
