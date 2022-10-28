# Harrison Holsinger
# Python Final
import pandas as pd

class Titanic:
    
    def __init__(self, Class: int, gender: str, stat: str):
        self.titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")
        self.Class = Class
        self.gender = gender
        self.stat = stat

# 1, 2, 3 class male average price of ticket        
    def firstClassMaleFare(self):
        firstClass = self.titanic.loc[(self.titanic['Pclass'] == 1)]
        firstClassMale = firstClass.loc[firstClass['Sex'] == 'male']
        avgFirstClassPriceM = firstClassMale ['Fare'].mean() 
        return '${:0,}'.format(round(avgFirstClassPriceM, 2))
    
    def secondClassMaleFare(self):
        secondClass = self.titanic.loc[(self.titanic['Pclass'] == 2)]
        secondClassMale = secondClass.loc[secondClass['Sex'] == 'male']
        avgSecondClassPriceM = secondClassMale ['Fare'].mean() 
        return '${:0,}'.format(round(avgSecondClassPriceM, 2))
    
    def thirdClassMaleFare(self):
        thirdClass = self.titanic.loc[(self.titanic['Pclass'] == 3)]
        thirdClassMale = thirdClass.loc[thirdClass['Sex'] == 'male']
        avgThirdClassPriceM = thirdClassMale ['Fare'].mean() 
        return '${:0,}'.format(round(avgThirdClassPriceM, 2))
    
# 1, 2, 3, class male average of age
    def firstClassMaleAge(self):
        firstClass = self.titanic.loc[(self.titanic['Pclass'] == 1)]
        firstClassMale = firstClass.loc[firstClass['Sex'] == 'male']
        avgFirstClassAgeM = firstClassMale ['Age'].mean() 
        return '{:0,}'.format(round(avgFirstClassAgeM))
    
    def secondClassMaleAge(self):
        secondClass = self.titanic.loc[(self.titanic['Pclass'] == 2)]
        secondClassMale = secondClass.loc[secondClass['Sex'] == 'male']
        avgSecondClassAgeM = secondClassMale ['Age'].mean() 
        return '{:0,}'.format(round(avgSecondClassAgeM))
    
    def thirdClassMaleAge(self):
        thirdClass = self.titanic.loc[(self.titanic['Pclass'] == 3)]
        thirdClassMale = thirdClass.loc[thirdClass['Sex'] == 'male']
        avgThirdClassAgeM = thirdClassMale ['Age'].mean() 
        return '{:0,}'.format(round(avgThirdClassAgeM))
    
# 1, 2, 3 class female average price of ticket        
    def firstClassFemaleFare(self):
        firstClass = self.titanic.loc[(self.titanic['Pclass'] == 1)]
        firstClassFemale = firstClass.loc[firstClass['Sex'] == 'female']
        avgFirstClassPriceF = firstClassFemale ['Fare'].mean() 
        return '${:0,}'.format(round(avgFirstClassPriceF, 2))
    
    def secondClassFemaleFare(self):
        secondClass = self.titanic.loc[(self.titanic['Pclass'] == 2)]
        secondClassFemale = secondClass.loc[secondClass['Sex'] == 'female']
        avgSecondClassPriceF = secondClassFemale ['Fare'].mean() 
        return '${:0,}'.format(round(avgSecondClassPriceF, 2))
    
    def thirdClassFemaleFare(self):
        thirdClass = self.titanic.loc[(self.titanic['Pclass'] == 3)]
        thirdClassFemale = thirdClass.loc[thirdClass['Sex'] == 'female']
        avgThirdClassPriceF = thirdClassFemale ['Fare'].mean() 
        return '${:0,}'.format(round(avgThirdClassPriceF, 2))
    
# 1, 2, 3, class female average of age
    def firstClassFemaleAge(self):
        firstClass = self.titanic.loc[(self.titanic['Pclass'] == 1)]
        firstClassFemale = firstClass.loc[firstClass['Sex'] == 'female']
        avgFirstClassAgeF = firstClassFemale ['Age'].mean() 
        return '{:0,}'.format(round(avgFirstClassAgeF))
    
    def secondClassFemaleAge(self):
        secondClass = self.titanic.loc[(self.titanic['Pclass'] == 2)]
        secondClassFemale = secondClass.loc[secondClass['Sex'] == 'female']
        avgSecondClassAgeF = secondClassFemale ['Age'].mean() 
        return '{:0,}'.format(round(avgSecondClassAgeF))
    
    def thirdClassFemaleAge(self):
        thirdClass = self.titanic.loc[(self.titanic['Pclass'] == 3)]
        thirdClassFemale = thirdClass.loc[thirdClass['Sex'] == 'female']
        avgThirdClassAgeF = thirdClassFemale ['Age'].mean() 
        return '{:0,}'.format(round(avgThirdClassAgeF))


def main():
    
    validClass = False
    validGender = False
    validStat = False
    validInput = False

    # Input validation
    while(validInput == False):
        
        try: 
              
            Class = int(input("Enter class choice(1, 2, or 3): "))
            gender = str(input("Enter gender selection(m or f): "))                
            stat = str(input("Enter statistic to be performed(age or fare): "))
        
        except Exception as err:
             print("Please enter an integer.")
             print(err)
        else:
            if Class == 1 or Class == 2 or Class == 3:
                validClass = True
            else:
                print("Please choose between 1, 2, or 3")
            if gender.lower() == 'm' or gender.lower() == 'f':
                validGender = True
            else:
                print("Please choose between m or f")
            if stat.lower() == "age" or stat.lower() == "fare":
                validStat = True
            else:
                print("Please choose between age or fare")
            if validClass == True and validGender == True and validStat == True:
                validInput = True    
    tit = Titanic(Class, gender, stat)

# 1, 2, 3 class of male ticket average
    if Class == 1 and gender == "m" and stat == "fare":
        print("Average first class male ticket price: " + tit.firstClassMaleFare())
    if Class == 2 and gender == "m" and stat == "fare":
        print("Average second class male ticket price: " + tit.secondClassMaleFare())        
    if Class == 3 and gender == "m" and stat == "fare":
        print("Average third class male ticket price: " + tit.thirdClassMaleFare()) 
    

# 1, 2, 3 class of male age average
    if Class == 1 and gender == "m" and stat == "age":
        print("Average first class male age: " + tit.firstClassMaleAge())
    if Class == 2 and gender == "m" and stat == "age":
        print("Average second class male age: " + tit.secondClassMaleAge())        
    if Class == 3 and gender == "m" and stat == "age":
        print("Average third class male age: " + tit.thirdClassMaleAge()) 

# 1, 2, 3 class of female ticket average
    if Class == 1 and gender == "f" and stat == "fare":
        print("Average first class female ticket price: " + tit.firstClassFemaleFare())
    if Class == 2 and gender == "f" and stat == "fare":
        print("Average second class female ticket price: " + tit.secondClassFemaleFare())      
    if Class == 3 and gender == "f" and stat == "fare":
        print("Average third class female ticket price: " + tit.thirdClassFemaleFare())
    
# 1, 2, 3 class of female age average    
    if Class == 1 and gender == "f" and stat == "age":
        print("Average first class female age: " + tit.firstClassFemaleAge())   
    if Class == 2 and gender == "f" and stat == "age":
         print("Average second class female age: " + tit.secondClassFemaleAge())       
    if Class == 3 and gender == "f" and stat == "age":
         print("Average third class female age: " + tit.thirdClassFemaleAge())
  

    
main()