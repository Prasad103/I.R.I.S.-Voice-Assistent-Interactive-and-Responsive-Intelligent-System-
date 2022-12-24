import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import webbrowser
from plyer import notification
from pygame import mixer
import speedtest
import six
import wolframalpha


#Library for Graphical User Interface
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer,QTime,QDate
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from jarvisSuperUI import Ui_Form



#Password protection
for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()                                                                                                                                                        
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

#Inrto video load 
from INTRO import cap
cap.release()




engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.TaskExection()


    def takeCommand(self):
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source,0,4)

        try:
            print("Understanding..")
            self.query  = r.recognize_google(audio,language='en-in')
            print(f"You Said: {self.query}\n")
        except Exception as e:
            print("Say that again")
            return "None"
        return self.query

    def alarm(query):
        timehere = open("Alarmtext.txt","a")
        timehere.write(query)
        timehere.close()
        os.startfile("alarm.py")


    def TaskExection(self):
        if __name__ == "__main__":
            while True:
                self.query = self.takeCommand().lower()
                if "wake up" in self.query:
                    from GreetMe import greetMe
                    greetMe()

                    while True:
                        self.query = self.takeCommand().lower()
                        if "go to sleep" in self.query:
                            speak("Ok sir , You can me call anytime")
                            break 

                        elif "change password" in self.query:
                            speak("What's the new password")
                            new_pw = input("Enter the new password\n")
                            new_password = open("password.txt","w")
                            new_password.write(new_pw)
                            new_password.close()
                            speak("Done sir")
                            speak(f"Your new password is{new_pw}")

                        elif "schedule my day" in self.query:
                            tasks = [] #Empty list 
                            speak("Do you want to clear old tasks (Plz speak YES or NO)")
                            self.query = self.takeCommand().lower()
                            if "yes" in self.query:
                                file = open("tasks.txt","w")
                                file.write(f"")
                                file.close()
                                no_tasks = int(input("Enter the no. of tasks :- "))
                                i = 0
                                for i in range(no_tasks):
                                    tasks.append(input("Enter the task :- "))
                                    file = open("tasks.txt","a")
                                    file.write(f"{i}. {tasks[i]}\n")
                                    file.close()
                            elif "no" in self.query:
                                i = 0
                                no_tasks = int(input("Enter the no. of tasks :- "))
                                for i in range(no_tasks):
                                    tasks.append(input("Enter the task :- "))
                                    file = open("tasks.txt","a")
                                    file.write(f"{i}. {tasks[i]}\n")
                                    file.close()

                        elif "show my schedule" in self.query:
                            file = open("tasks.txt","r")
                            content = file.read()
                            file.close()
                            mixer.init()
                            mixer.music.load("notification.mp3")
                            mixer.music.play()
                            notification.notify(
                                    title = "My schedule :-",
                                    message = content,
                                    timeout = 15
                                    )

                        elif "open" in self.query:   
                            self.query = self.query.replace("open","")
                            self.query = self.query.replace("jarvis","")
                            self.query = self.query.replace("iris","")
                            pyautogui.press("super")
                            pyautogui.typewrite(self.query)
                            pyautogui.sleep(2)
                            pyautogui.press("enter")

                        elif "internet speed" in self.query:
                            wifi  = speedtest.Speedtest()
                            upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                            download_net = wifi.download()/1048576
                            print("Wifi Upload Speed is", upload_net)
                            print("Wifi download speed is ",download_net)
                            speak(f"Wifi download speed is {download_net}")
                            speak(f"Wifi Upload speed is {upload_net}")

                        elif "translate" in self.query:
                            from Translator import translategl
                            self.query = self.query.replace("jarvis","")
                            self.query = self.query.replace("translate","")
                            translategl(self.query)


                        elif "hello" in self.query:
                            speak("Hello sir, how are you ?")
                        elif "i am fine" in self.query:
                            speak("that's great, sir")
                        elif "how are you" in self.query:
                            speak("Perfect, sir")
                        elif "thank you" in self.query:
                            speak("you are welcome, sir")
                        elif "who are you" in self.query:
                            speak("i am iris , interactive and responsive intellegent system")

                        elif "tired" in self.query:
                            speak("Playing your favourite songs, sir")
                            a = (1,2,3) 
                            b = random.choice(a)
                            if b==1:
                                webbrowser.open("https://www.youtube.com/watch?v=W1S9AbHpWFY")
                            elif b==2:
                                webbrowser.open("https://www.youtube.com/watch?v=mNuhKUOD_A0")

                        elif "pause" in self.query:
                            pyautogui.press("k")
                            speak("video paused")
                        elif "play" in self.query:
                            pyautogui.press("k")
                            speak("video played")
                        elif "mute" in self.query:
                            pyautogui.press("m")
                            speak("video muted")

                        elif "volume up" in self.query:
                            from keyboard import volumeup
                            speak("Turning volume up,sir")
                            volumeup()
                        elif "volume down" in self.query:
                            from keyboard import volumedown
                            speak("Turning volume down, sir")
                            volumedown()

                        elif "open" in self.query:
                            from Dictapp import openappweb
                            openappweb(self.query)
                        elif "close" in self.query:
                            from Dictapp import closeappweb
                            closeappweb(self.query)

                        elif "google" in self.query:
                            from SearchNow import searchGoogle
                            searchGoogle(self.query)
                        elif "youtube" in self.query:
                            from SearchNow import searchYoutube
                            searchYoutube(self.query)
                        elif "wikipedia" in self.query:
                            from SearchNow import searchWikipedia
                            searchWikipedia(self.query)

                        elif "news" in self.query:
                            from NewsRead import latestnews
                            latestnews()

                        elif "calculate" in self.query:
                            from Calculatenumbers import WolfRamAlpha
                            from Calculatenumbers import Calc
                            self.query = self.query.replace("calculate","")
                            self.query = self.query.replace("jarvis","")
                            Calc(self.query)

                        elif "whatsapp" in self.query:
                            from Whatsapp import sendMessage
                            sendMessage()

                        elif "temperature" in self.query:
                            search = "temperature in satara"
                            url = f"https://www.google.com/search?q=tempeartur+in+satara&rlz=1C1CHBF_enIN1021IN1021&oq={search}"
                            r  = requests.get(url)
                            data = BeautifulSoup(r.text,"html.parser")
                            temp = data.find("div", class_ = "BNeawe").text
                            speak(f"current{search} is {temp}")

                        elif "weather" in self.query:
                            search = "temperature in satara"
                            url = f"https://www.google.com/search?q=tempeartur+in+satara&rlz=1C1CHBF_enIN1021IN1021&oq={search}"
                            r  = requests.get(url)
                            data = BeautifulSoup(r.text,"html.parser")
                            temp = data.find("div", class_ = "BNeawe").text
                            speak(f"current{search} is {temp}")

                        elif "set an alarm" in self.query:
                            print("input time example:- 10 and 10 and 10")
                            speak("Set the time")
                            a = input("Please tell the time :- ")
                            self.alarm(a)
                            speak("Done,sir")

                        elif "the time" in self.query:
                            strTime = datetime.datetime.now().strftime("%H:%M")    
                            speak(f"Sir, the time is {strTime}")

                        elif "finally sleep" in self.query:
                            speak("Going to sleep,sir")
                            exit()

                        elif "remember that" in self.query:
                            rememberMessage = self.query.replace("remember that","")
                            rememberMessage = self.query.replace("jarvis","")
                            speak("You told me to remember that"+rememberMessage)
                            remember = open("Remember.txt","a")
                            remember.write(rememberMessage)
                            remember.close()
                        elif "what do you remember" in self.query:
                            remember = open("Remember.txt","r")
                            speak("You told me to remember that" + remember.read())

                        elif "shutdown the system" in self.query:
                            speak("Are You sure you want to shutdown")
                            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                            if shutdown == "yes":
                                os.system("shutdown /s /t 1")
                            elif shutdown == "no":
                                break



startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.startPushButton.clicked.connect(self.startTask)
        self.ui.quitPushButton.clicked.connect(self.close)

    def startTask(self):
        
        self.ui.movie = QtGui.QMovie("./GUI files/Siri.gif")
        self.ui.jarvisGUI.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("./GUI files/Code_Template.gif")
        self.ui.ironManBackground.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("./GUI files/Iron_Template_1.gif")
        self.ui.ironManGIF.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("./GUI files/gggf.jpg")
        self.ui.dateLabel.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("./GUI files/gggf.jpg")
        self.ui.timeLabel.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("./GUI files/Start.png")
        self.ui.startLabelNotButton.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("./GUI files/Quit.png")
        self.ui.quitLabelNotButton.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("./GUI files/Ntuks.gif")
        self.ui.earthGIF.setMovie(self.ui.movie)
        self.ui.movie.start()


        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        currentTime = QTime.currentTime()
        currentDate = QDate.currentDate()
        labelTime = currentTime.toString('hh:mm:ss')
        labelDate = currentDate.toString(Qt.ISODate)
        self.ui.dateTextBrowser.setText(f"Date: {labelDate}")
        self.ui.timeTextBrowser.setText(f"Time: {labelTime}")

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())