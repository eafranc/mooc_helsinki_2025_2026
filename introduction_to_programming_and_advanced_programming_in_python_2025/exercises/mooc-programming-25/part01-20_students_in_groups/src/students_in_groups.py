# Write your solution here
students   = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))

# My line of reasoning:

# n = q*d + r

# - The remainder r is an integer between 0 and (d-1), in which d is the divisor
# - I need a calculation that:
# -- Adds 0 to the quotient (q) if it is an even division (r==0)
# -- Adds 1 to the quotient (q) if it is a division with remainder (r!=0)

# The hack is to add to the division the greatest possible remainder, (d-1); Looking r:
#- If r!=0, (d-1) will add 1 to q in the integer division (//)
#- If r==0, (d-1) won't be able to add 1 to q in the integer division (//)

# A - When r==0 ==> n = q*d 
# [n + (d-1)]//d = [q*d + (d-1)]//d  = [q*d//d] + [(d-1)//d] = q + 0
# So, [n + (d-1)]//d = q

# B - When r!= 0 ==> 0 < r <= d-1 and n =  q*d + r
# [n + (d-1)]//d = [(q*d + r) + (d-1)]//d  = [q*d//d] + [r + (d-1)//d]

# Since (d-1) < r + (d-1) <= 2*(d-1) ==> (d-1)//d = 0 < [r + (d-1)//d] <= 2*(d-1)//d 
# Note that 2*(d-1)//d = (d)//d + (d-2)//d = 1 + 0 
# Thus, 0 < [r + (d-1)//d] <= 1 ==> [r + (d-1)//d] = 1
# So, [n + (d-1)]//d = q + 1

### CONCLUSION: in order to make our calculation have the behavior mentioned above, add (d-1) to the integer division


print(f"Number of groups formed: {((students + (group_size - 1)) // group_size)}")