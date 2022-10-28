golfScoreFile = open('golfRecords.txt','r')

for i in range(12):
    line = golfScoreFile.readline()
    if line.isdigit():
        print("Score:", line)
    else:
        print("Name:", line)
       
