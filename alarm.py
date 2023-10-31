from tkinter import *  
import datetime as dt  
import time  
from playsound import playsound
# import winsound as ws  
  
# defining the function for the alarm clock  
def alarm(setAlarmTimer): 
    print("wait for the alaram!") 
    while True:  
        time.sleep(1)  
        actualTime = dt.datetime.now()  
        currentTime = actualTime.strftime("%H : %M : %S")  
        currentDate = actualTime.strftime("%d / %m / %Y")   
        if currentTime == setAlarmTimer:  
            playsound("sounds.wav")
            break  
  
def getAlarmTime():  
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"  
    alarm(alarmSetTime)  
  
# creating the GUI for the application  
guiWindow = Tk()  
guiWindow.title("The Alarm Clock")  
guiWindow.geometry("464x200")  
guiWindow.config(bg = "#800080")  
guiWindow.resizable(width = False, height = False)  
   
timeFormat = Label(  
    guiWindow,  
    text = "Remember to set time in 24-hour format!",  
    fg = "white",  
    bg = "#4169e1",  
    font = ("Arial", 15)  
    ).place(  
        x = 0,  
        y = 160  
        )  
   
add_time = Label(  
    guiWindow,  
    text = "Hour     Minute     Second",  
    font = 60,  
    fg = "white",  
    bg = "#800080"  
    ).place(  
        x = 220,  
        y = 10  
        )  
  
setAlarm = Label(  
    guiWindow,  
    text = "Set Time for Alarm: ",  
    fg = "white",  
    bg = "#FF7F50",  
    relief = "solid",  
    font = ("Helevetica", 13, "bold")  
    ).place(  
        x = 5,  
        y = 50  
        )  
   
hour = StringVar()  
minute = StringVar()  
second = StringVar()  
   
hourTime = Entry(  
    guiWindow,  
    textvariable = hour,  
    bg = "#FF69B4",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 220,  
        y = 53  
        )  
minuteTime = Entry(  
    guiWindow,  
    textvariable = minute,  
    bg = "#FF69B4",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 297,  
        y = 53  
        )  
secondTime = Entry(  
    guiWindow,  
    textvariable = second,  
    bg = "#FF69B4",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 390,  
        y = 53  
        )  
   
submit = Button(  
    guiWindow,  
    text = "Set The Alarm",  
    fg = "white",  
    bg = "#4169e1",  
    width = 15,  
    command = getAlarmTime,  
    font = (20)  
    ).place(  
        x = 140,  
        y = 100  
        )  
   
guiWindow.mainloop()  