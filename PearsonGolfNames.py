num_players = int(input("Enter number of players:"))
golfScoreFile = open('golfRecords.txt','w')

for i in range(num_players):
    Name = input("Enter name of player number " + str(i + 1) + ":")
    Score = int(input("Enter score of player number " + str(i + 1) + ":"))
    golfScoreFile.write(Name + "\n")
    golfScoreFile.write(str(Score) + "\n")
    i += 1