# Harrison Holsinger
# This program takes in three digits and prints the highest, lowest, and then 
# divides x/y

# Inputs
x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))
z = int(input("Enter the value for z: "))

# Calculate lowest
if x < y and x < z:
    print("Lowest: x")
elif y < x and y < z:
    print("Lowest: y")
elif z < y and z < x:
    print("Lowest: z")
    
# Calcualte highest
if x > y and x > z:
    print("Highest: x")
elif y > x and y > z:
    print("Highest: y")
elif z > y and z > x:
    print("Highest: z")

# Make sure y is not 0, then divide x/y
if y == 0:
    print("Error: Cannot divide by zero")
else:
    div =str(round(x/y, 2))
    print("x/y = " + div)
 
print("Goodbye")