import os
import datetime
import pyttsx3
engine = pyttsx3.init()

def startup():
    f = open('medicine.txt', 'a')
    print("welcome to RemindBot!")
    while True:
        medicine = input("Input medication: ")
        interval = input("You take this medication every how many hours?    ")
        print("you take {} every {} hours" .format(medicine, interval))
        text = "{},{}\n".format(medicine, interval)
        f.write(text)
        cont = input("do you need to add more medication? y/n: ")
        if cont == "n":
            f.close()
            break



def set_time():
    #f = open('medicine.txt', 'r')
    now = datetime.datetime.now()
    cur_time = now.strftime("%H:%M")
    if cur_time == "05:48":
        engine.say("it is time to take your medicine")
        engine.runAndWait()
    print("time is", cur_time)
    #f.close()
    


set_time()    



