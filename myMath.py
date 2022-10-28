import math

# Harrison Holsinger
# myMath.py
# This program will produce a menu of calculator options for the user to select
# from. The user will also get to select the numbers for those calculations. A 
# function will be called and return the answer, as well as loop until the user
# quits.

# Takes in two paramenters, adds them together, returns result
def add(x, y):
    result = x + y
    print(str(x) + " + " + str(y) + " = " + str(result))   
    
# Takes in two paramenters, subtracts them, returns result   
def sub(x, y):
    result = x - y
    print(str(x) + " - " + str(y) + " = " + str(result))  

# Takes in two paramenters, multiplies them, returns result
def multiply(x, y):
    result = x * y
    print(str(x) + " * " + str(y) + " = " + str(result))  
    
# Takes in two paramenters, divides them, returns result
def divide(x, y):
    result = x / y
    print(str(x) + " / " + str(y) + " = " + str(round(result, 2)))  
 
# Takes in two paramenters, calculates modulus, returns result
def mod(x, y):
    result = x % y
    print(str(x) + " % " + str(y) + " = " + str(result))  

# Takes in one paramenters, finds square root, returns result
def sqrt(x):
    result = math.sqrt(x)
    print("sqrt of " + str(x) + " = " + str(round(result, 2)))  

# Giant loop
loop = True
while(loop == True):
    # Menu
    print("")
    print("### Welcome to My Calculator ###")
    print("1. Add(x,y)")
    print("2. Subtract(x,y)")
    print("3. Multiply(x,y)")
    print("4. Divide(x,y)")
    print("5. Mod(x,y)")
    print("6. Sqrt(x)")
    print("7. Exit")
    
    validChoice = False

    # Menu Choice Validation
    while(validChoice == False):
        try:
            choice = int(input("Enter here: "))    
        except Exception as err:
            print("Please enter an integer.")
            print(err)
        else:
            if choice > 7 or choice < 1:
                print("Enter a number presented in the menu.")
            else:
                validChoice = True
                
    # Enter 7 to exit program       
    if choice == 7:
        print("Thanks for using MyCalculator!")
        break
                
    validX = False

    # X validation
    while(validX == False):
        try:
            choiceX = int(input("Enter x: "))    
        except Exception as err:
            print("Please enter an integer.")
            print(err)
        else:
            if choiceX < 0:
                print("Enter a number greater than or equal to zero.")
            else:
                validX = True
   
    validY = False
    # If the user wants to find the sqrt, no Y value is needed
    if choice == 6:
        validY = True

    # Y validation
    while(validY == False):
        try:
            choiceY = int(input("Enter y: "))    
        except Exception as err:
            print("Please enter an integer.")
            print(err)
        else:
            if choiceY < 0:
                print("Enter a number greater than or equal to zero.")
            # If the user wants to divide, they can no longer enter zero for the Y value
            elif choice == 4 and choiceY == 0:
                print("Enter a number greater than zero.")
            else:
                validY = True
    
    # Function calls
    print("")
    if choice == 1:
        add(choiceX, choiceY)
    elif choice == 2:
        sub(choiceX, choiceY)
    elif choice == 3:
        multiply(choiceX, choiceY)
    elif choice == 4:
        divide(choiceX, choiceY)
    elif choice == 5:
        mod(choiceX, choiceY)
    elif choice == 6:
        sqrt(choiceX)
        
        
        
        
        
        
        
        
        
        