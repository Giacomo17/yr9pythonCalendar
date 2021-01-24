#imports
#pip3 install tkcalendar
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
import datetime 

#window setup
#Root will be the window used for the program
#Window will be the one used for the guide

window = tk.Tk()
window.title("Guide")
window.geometry("975x230")


root = tk.Tk()
root.title("Calendar and Task Manager")
root.minsize(1200,1000)
root.maxsize(1200,1000)
root.geometry("1200x1000")
          
#set up which DD/MM/YY it is 
#Get the reall date using datetime then decode it into a var to be used in setting the date
today = datetime.datetime.now()
tdyear = today.year
tdmonth = today.month
tdday = today.day

#Guide Window
#Use multiple lines to not have to make the window obnoxiously big
Line1= tk.Label(window, text="Welcome." )
Line1.place(x=10, y=10)
Line2= tk.Label(window, text="The program is a Calendar and task manager, You are able to imput a Task and using the calendar select which day it falls on.")
Line2.place(x=10, y=60)
Line3= tk.Label(window, text="To select a day simply click on it in the Calendar to make sure it is selected the number will be yellow. To name the task input the name in the Input Box. ")
Line3.place(x=10, y=110)
Line4= tk.Label(window, text="To add the task press the large plus button to the right of the input box or press enter. To delete press the Delete this task button. ")
Line4.place(x=10, y=160)
#calendar setup
#Cal is the calendar names year, month and day is to have today's date the day that automatically open with
cal = Calendar(root, selectmode="day", year=(tdyear), month=(tdmonth), day=(tdday),
	firstweekday= "sunday",
	showweeknumbers= False, 
	foreground= "black",
	background= "grey",
	selectforeground= "yellow",
	selectbackground= "orange"
	)
cal.place(height=950, width=750,)
#This was is a test to make sure that the set day command works
print(cal.get_date())


#Each of these are just reseting the result for the _ task whent the command deletetask_ is made through a button
def deletetask1():
	result1 = "	"
	result1Label.config(text=result1)

def deletetask2():
	result2 = "	"
	result2Label.config(text=result2)

def deletetask3():
	result3 = "	"
	result3Label.config(text=result3)

def deletetask4():
	result4 = "	"
	result4Label.config(text=result4)

def deletetask5():
	result5 = "	"
	result5Label.config(text=result5)

def deletetask6():
	result6 = "	"
	result6Label.config(text=result6)

def deletetask7():
	result7 = "	"
	result7Label.config(text=result7)

def deletetask8():
	result8 = "	"
	result8Label.config(text=result8)

def deletetask9():
	result9 = "	"
	result9Label.config(text=result9)

def deletetask10():
	result10 = "	"
	result10Label.config(text=result10)

#These are the oppistite this creates the task according to the date which is found by cal.get_date and the entry of the corresponding tasks

def addtask1(arg=None):

    result1 = taskentry1.get()
    result1Label.config(bg= "#fffdd0", text=result1 + " " + cal.get_date())
    taskentry1.delete(0,END)

def addtask2(arg=None):

	result2 = taskentry2.get()
	result2Label.config(bg= "#fffdd0", text=result2 + " " + cal.get_date())
	taskentry2.delete(0,END)

def addtask3(arg=None):

	result3 = taskentry3.get()
	result3Label.config(bg= "#fffdd0", text=result3 + " " + cal.get_date())
	taskentry3.delete(0,END)

def addtask4(arg=None):

	result4 = taskentry4.get()
	result4Label.config(bg= "#fffdd0", text=result4 + " " + cal.get_date())
	taskentry4.delete(0,END)

def addtask5(arg=None):

	result5 = taskentry5.get()
	result5Label.config(bg= "#fffdd0", text=result5 + " " + cal.get_date())
	taskentry5.delete(0,END)

def addtask6(arg=None):

	result6 = taskentry6.get()
	result6Label.config(bg= "#fffdd0", text=result6 + " " + cal.get_date())
	taskentry6.delete(0,END)

def addtask7(arg=None):

	result7 = taskentry7.get()
	result7Label.config(bg= "#fffdd0", text=result7 + " " + cal.get_date())
	taskentry7.delete(0,END)

def addtask8(arg=None):

	result8 = taskentry8.get()
	result8Label.config(bg= "#fffdd0", text=result8 + " " + cal.get_date())
	taskentry8.delete(0,END)

def addtask9(arg=None):

	result9 = taskentry9.get()
	result9Label.config(root, bg= "#fffdd0", text=result9 + " " + cal.get_date())
	taskentry9.delete(0,END)

def addtask10(arg=None):

	result10 = taskentry10.get()
	result10Label.config(bg= "#fffdd0", text=result10 + " " + cal.get_date())
	taskentry10.delete(0,END)

#this is the entry for the tasks it allows any character and an ulimateed amount of them
taskentry1 = tk.Entry(root, width="10")
taskentry1.focus()
taskentry1.bind("<Return>", addtask1)
addtask1 = tk.Button(root, text= "Enter", command=addtask1)

#the results labels are just where the should be and the intail state they are in when the program is opened
result1Label = tk.Label(root, text = "")
result1Label.place(x=760, y=60)


taskentry1.place(x=920, y= 60)

taskentry2 = tk.Entry(root, width="10")
taskentry2.focus()
taskentry2.bind("<Return>", addtask2)
addtask2 = tk.Button(root, text= "Enter", command=addtask2)


result2Label = tk.Label(root, text = "")
result2Label.place(x=760, y=110)

taskentry2.place(x=920, y= 110)

taskentry3 = tk.Entry(root, width="10")
taskentry3.focus()
taskentry3.bind("<Return>", addtask3)
addtask3 = tk.Button(root, text= "Enter", command=addtask3)


result3Label = tk.Label(root, text = "")
result3Label.place(x=760, y=160)

taskentry3.place(x=920, y= 160)

taskentry4 = tk.Entry(root, width="10")
taskentry4.focus()
taskentry4.bind("<Return>", addtask4)
addtask4 = tk.Button(root, text= "Enter", command=addtask4)


result4Label = tk.Label(root, text = "")
result4Label.place(x=760, y=210)

taskentry4.place(x=920, y= 210)


taskentry5 = tk.Entry(root, width="10")
taskentry5.focus()
taskentry5.bind("<Return>", addtask5)
addtask5 = tk.Button(root, text= "Enter", command=addtask5)


result5Label = tk.Label(root, text = "")
result5Label.place(x=760, y=260)

taskentry5.place(x=920, y= 260)

taskentry6 = tk.Entry(root, width="10")
taskentry6.focus()
taskentry6.bind("<Return>", addtask6)
addtask6 = tk.Button(root, text= "Enter", command=addtask6)


result6Label = tk.Label(root, text = "")
result6Label.place(x=760, y=310)

taskentry6.place(x=920, y= 310)

taskentry7 = tk.Entry(root, width="10")
taskentry7.focus()
taskentry7.bind("<Return>", addtask7)
addtask7 = tk.Button(root, text= "Enter", command=addtask7)


result7Label = tk.Label(root, text = "")
result7Label.place(x=760, y=360)

taskentry7.place(x=920, y= 360)


taskentry8 = tk.Entry(root, width="10")
taskentry8.focus()
taskentry8.bind("<Return>", addtask8)
addtask8 = tk.Button(root, text= "Enter", command=addtask8)


result8Label = tk.Label(root, text = "")
result8Label.place(x=760, y=410)

taskentry8.place(x=920, y= 410)

taskentry9 = tk.Entry(root, width="10")
taskentry9.focus()
taskentry9.bind("<Return>", addtask9)
addtask9 = tk.Button(root, text= "Enter", command=addtask9)


result9Label = tk.Label(root, text = "")
result9Label.place(x=760, y=460)

taskentry9.place(x=920, y= 460)

taskentry10 = tk.Entry(root, width="10")
taskentry10.focus()
taskentry10.bind("<Return>", addtask10)
addtask10 = tk.Button(root, text= "Enter", command=addtask10)


result10Label = tk.Label(root, text = "")
result10Label.place(x=760, y=510)

taskentry10.place(x=920, y= 510)

#this is all of the buttons and the commands that will prompt the creation or removal of a task

addtask1 = tk.Button(root, bg="yellow", height="2", width="2", text="+", font="Helvetica 16", command=addtask1)
addtask2 = tk.Button(root, bg="yellow", height="2", width="2", text="+", font="Helvetica 16", command=addtask2)
addtask3 = tk.Button(root, bg="yellow", height="2", width="2", text="+", font="Helvetica 16", command=addtask3)
addtask4 = tk.Button(root, bg="yellow", height="2", width="2", text="+", font="Helvetica 16", command=addtask4)
addtask5 = tk.Button(root, bg="yellow", height="2", width="2", text="+", font="Helvetica 16", command=addtask5)
addtask6 = tk.Button(root, bg="yellow", height="2", width="2", text="+", font="Helvetica 16", command=addtask6)
addtask7 = tk.Button(root, bg="yellow", height="2", width="2", text="+", font="Helvetica 16", command=addtask7)
addtask8 = tk.Button(root, bg="yellow", height="2", width="2", text="+", font="Helvetica 16", command=addtask8)
addtask9= tk.Button(root, bg="yellow", height="2", width="2", text="+", font="Helvetica 16", command=addtask9)
addtask10 = tk.Button(root, bg="yellow", height="2", width="2", text="+", font="Helvetica 16", command=addtask10)


deltask1 = tk.Button(root, bg="#ffcccb", command=deletetask1, text="Delete Task 1")
deltask2 = tk.Button(root, bg="#ffcccb", command=deletetask2, text="Delete Task 2")
deltask3 = tk.Button(root, bg="#ffcccb", command=deletetask3, text="Delete Task 3")
deltask4 = tk.Button(root, bg="#ffcccb", command=deletetask4, text="Delete Task 4")
deltask5 = tk.Button(root, bg="#ffcccb", command=deletetask5, text="Delete Task 5")
deltask6 = tk.Button(root, bg="#ffcccb", command=deletetask6, text="Delete Task 6")
deltask7 = tk.Button(root, bg="#ffcccb", command=deletetask7, text="Delete Task 7")
deltask8 = tk.Button(root, bg="#ffcccb", command=deletetask8, text="Delete Task 8")
deltask9 = tk.Button(root, bg="#ffcccb", command=deletetask9, text="Delete Task 9")
deltask10 = tk.Button(root, bg="#ffcccb", command=deletetask10, text="Delete Task 10")

#this is where all of the task are placed 
#I tried to make the placement values as even as possible so expansion math would be easy

deltask1.place(x= 1100, y= 50)
deltask2.place(x= 1100, y= 100)
deltask3.place(x= 1100, y= 150)
deltask4.place(x= 1100, y= 200)
deltask5.place(x= 1100, y= 250)
deltask6.place(x= 1100, y= 300)
deltask7.place(x= 1100, y= 350)
deltask8.place(x= 1100, y= 400)
deltask9.place(x= 1100, y= 450)
deltask10.place(x= 1100, y= 500)

addtask1.place(x= 1025, y= 50)
addtask2.place(x= 1025, y= 100)
addtask3.place(x= 1025, y= 150)
addtask4.place(x= 1025, y= 200)
addtask5.place(x= 1025, y= 250)
addtask6.place(x= 1025, y= 300)
addtask7.place(x= 1025, y= 350)
addtask8.place(x= 1025, y= 400)
addtask9.place(x= 1025, y= 450)
addtask10.place(x= 1025, y= 500)

#Ending the tkinter program

window.mainloop()
root.mainloop()