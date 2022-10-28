# Harrison Holsinger
# Python Midterm Exam

def avg(list):
    total = 0
    for i in list:
        total += i
    avg = total / len(list)
    return avg

def lowestScore(list):
    list.sort()
    list.pop(0)
    total = 0
    for i in list:
        total += i
    avg = total / len(list)
    return avg

validInteger1 = False
validInteger2 = False
validInteger3 = False
validInteger = False


while(validInteger == False):
    try: 
        score1 = int(input("Enter score 1:"))
        score2 = int(input("Enter score 2:"))
        score3 = int(input("Enter score 3:"))
    except Exception as err:
         print("Please enter an integer.")
         print(err)
    else:
         
        list = []
        
        list.append(score1)
        list.append(score2)
        list.append(score3)
        
                
        if list[0] < 100 and list[0] > 0:
            validInteger1 = True
        else:
            print("Please enter a number between 0 and 100")
        if list[1] < 100 and list[1] > 0:
            validInteger2 = True
        else:
            print("Please enter a number between 0 and 100")
        if list[2] < 100 and list[2] > 0:
            validInteger3 = True
        else:
            print("Please enter a number between 0 and 100")
        if validInteger1 == True and validInteger2 == True and validInteger3 == True:
            validInteger = True

print("")
print("Average: ", round(avg(list), 2))
print("Average without lowest score:", round(lowestScore(list), 2))



   
     