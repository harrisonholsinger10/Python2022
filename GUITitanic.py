# Harrison Holsinger
# GIU Titanic Program with tkinter

from tkinter import *
from tkinter import messagebox
import pandas as pd

# create root window
root = Tk()
 
# root window title and dimension
root.title("Titanic GUI Program")
# Set geometry (widthxheight)
root.geometry('350x500')
 
# Import Titanic Data set
titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

# Filter first class out of data set. Average ticket cost and age
firstClass = titanic.loc[(titanic['Pclass'] == 1)]
avgFirstClassPrice = firstClass ['Fare'].mean() 
avgFirstClassAge = firstClass ['Age'].mean() 

# Filter second class out of data set. Average ticket cost and age
secondClass = titanic.loc[(titanic['Pclass'] == 2)]
avgSecondClassPrice = secondClass ['Fare'].mean() 
avgSecondClassAge = secondClass ['Age'].mean() 

# Filter third class out of data set. Average ticket cost and age
thirdClass = titanic.loc[(titanic['Pclass'] == 3)]
avgThirdClassPrice = thirdClass ['Fare'].mean() 
avgThirdClassAge = thirdClass ['Age'].mean() 

# Create title and label
lbl = Label(root, text = "Titanic Average Calculator", font = ('Times 24'))
lbl.grid()
lbl2 = Label(root, text = "Choose from the following options:", font = ('Times 14'))
lbl2.grid()

lbl3 = Label(root, text = "")

# Define functions
def class1Ticket():
    lbl3 = Label(root, text = "The average First Class Ticket was " + '${:0,}'.format(round(avgFirstClassPrice, 2)), fg = "blue", font = 'bold')
    lbl3.grid()
def class2Ticket():
    lbl4 = Label(root, text = "The average Second Class Ticket was " + '${:0,}'.format(round(avgSecondClassPrice, 2)), fg = "red", font = 'bold')
    lbl4.grid()
def class3Ticket():
    lbl5 = Label(root, text = "The average Third Class Ticket was " + '${:0,}'.format(round(avgThirdClassPrice, 2)), fg = "green", font = 'bold')
    lbl5.grid()
def class1Age():
    lbl6 = Label(root, text = "The average First Class Age was " + '{:0,}'.format(round(avgFirstClassAge, 0)), fg = "purple", font = 'bold')
    lbl6.grid()
def class2Age():
    lbl7 = Label(root, text = "The average Second Class Age was " + '{:0,}'.format(round(avgSecondClassAge, 0)), fg = "orange", font = 'bold')
    lbl7.grid()
def class3Age():
    lbl8 = Label(root, text = "The average Third Class Age was " + '{:0,}'.format(round(avgThirdClassAge, 0)), fg = "pink", font = 'bold')
    lbl8.grid()
    
# Set radio buttons and variables
var = IntVar()
var.set("")
r1 = Radiobutton(root, text='First Class Ticket Average', value=1, variable=var, tristatevalue=0, command = lambda: class1Ticket())
r2 = Radiobutton(root, text='Second Class Ticket Average', value=2, variable=var, tristatevalue=0, command = lambda: class2Ticket())
r3 = Radiobutton(root, text='Third Class Ticket Average', value=3, variable=var, tristatevalue=0, command = lambda: class3Ticket())
r4 = Radiobutton(root, text='First Class Age Average', value=4, variable=var, tristatevalue=0, command = lambda: class1Age())
r5 = Radiobutton(root, text='Second Class Age Average', value=5, variable=var, tristatevalue=0, command = lambda: class2Age())
r6 = Radiobutton(root, text='Third Class Age Average', value=6, variable=var, tristatevalue=0, command = lambda: class3Age())

# Put radio buttons on grid
r1.grid()
r2.grid()
r3.grid()
r4.grid()
r5.grid()
r6.grid()

# Execute Tkinter
root.mainloop()