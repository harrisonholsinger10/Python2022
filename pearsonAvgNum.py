avg_nums = open("numbers.txt",'r')

total = 0
numberoflines=0
average = 0
#line = avg_nums.readline()

for line in avg_nums:
    for word in line.split():
        if word.isdigit() == True:
            number = float(line)
            total += number
            numberoflines += 1
   

average = total/numberoflines
print(str(average))

avg_nums.close()
