import random
# squareList.py
# Harrison Holsinger
# This program will randomly create a list, pass it through a function that
# will square every number in that list

# Function square: squares values in a list
def square(list):
    # Creat an empty list for squared values
    listSquare = []
    # Loop through old list, square each value
    for i in range(len(list)):
        listSquare.insert(i, list[i] * list[i])
        i += 1
    return listSquare
 
# Create a random length 3-10 of the list       
length = random.randint(3, 10)
list = []

# Loop through the list, assign a random int 1-25 for each element in the list
for x in range(length):
    num = random.randint(1, 25)
    list.append(num)
    list.sort()

# Print list
print(list)

# Call and print square function
print(square(list))


