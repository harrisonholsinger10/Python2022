# Time Calculator Part II

validInteger = False

while(validInteger == False):
    try:
        seconds = int(input("Enter a number of seconds: "))
    except Exception as err:
        print("Please enter an integer.")
        print(err)
    else:
        if seconds <= 0:
            print("Enter a number greater than 0")
            validInteger = False
        else:
            ValidInteger = True
        

days = int(seconds / 86400)
seconds = seconds % 86400
print(str(days) + " days")

hours = int(seconds / 3600)
seconds = seconds % 3600
print(str(hours) + " hours")

minutes = int(seconds / 60)
seconds = seconds % 60
print(str(minutes) + " minutes")
print(str(seconds) + " seconds")
