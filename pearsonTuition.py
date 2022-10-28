tuition = 8000.00
rate = 0.03 * tuition
i = 1
while i <= 5:
    tuition = round(tuition * 1.03, 2)
    if i == 1:
        print("In " + str(i) + " year, the tuition will be " + "${:.2f}".format(tuition) + ".") 
    if i > 1:
        print("In " + str(i) + " years, the tuition will be " + "${:.2f}".format(tuition) + ".") 
    i += 1
    

