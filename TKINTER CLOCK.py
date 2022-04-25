# BASIC ALARM CLOCK USING TKINTER


#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import winsound
import datetime
import time



#Alarm method loops through the current time second by second in the terminal
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.Currenttime()
        Currenttime = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The current Date is:",date)   #current date
        print(Currenttime)   #prints time second by second 
        if Currenttime == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)    #plays the default current sound
            break
#sets alarm
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()  #imports tkinter into an object
clock.title("Basic Alarm Clock")

clock.geometry("600x300")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="white",bg="black",font="Sans").place(x=60,y=120)
addTime = Label(clock,text = "Hours  Minutes   Seconds",font=80).place(x = 160)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

# Variables required to set alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required
hourTime= Entry(clock,textvariable = hour,bg = "skyblue",width = 20).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "skyblue",width = 20).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "skyblue",width = 20).place(x=200,y=30)

#To take the time input by user:
SET = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)

clock.mainloop()
#Execution

