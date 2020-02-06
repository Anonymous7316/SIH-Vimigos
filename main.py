import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon,QImage, QPalette, QBrush
from PyQt5.QtCore import pyqtSlot, QSize
from PyQt5 import QtCore
from modules.web import *
from modules.fun import *
from database.database import mailtoname,nametomail
import os
import threading as thread
from modules.record.recording import *
from modules.record.record_to_text import conv
import speech_recognition as sr
import win32com.client as wincl
from modules.wiki import wikip
from modules.chatbot import *
from modules.calculator import *
from face_rec.face_set import face_rec_main
import aiml
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import json
from difflib import get_close_matches
import datetime 
import smtplib
k = aiml.Kernel()
k.learn("database/std-startup.xml")
k.respond("load aiml b")
data = json.load(open("database/data.json"))

speak = wincl.Dispatch("SAPI.SpVoice")
spee = speak.Speak
def spppp(q):
        print(q)
        spee(q)
def send_mail(add,data):
        try:
                s = smtplib.SMTP('smtp.gmail.com', 587) 
                s.starttls() 

                ###################################################################################
                s.login("Your email id","Your password")
                #################################################################################

                s.sendmail("your email id",add,data)
                s.quit
                return "mail sent to "+add
        except:
                return "Please check your internet connection"

def extras_spam(n):
    q = k.respond(n)
    if q =="damm":
        q = response(n)
        if q == "not got":
                webbrowser.open('www.google.com/search?q='+n)
                q = "Not got! Searching on web."
                return q
        else:
                return q
    else:
        return q

def dictionarry(w):  
    if w in data:
        return data[w][0]
    elif w.title() in data:
        return data[w.title()][0]
    elif len(get_close_matches(w, data.keys())) > 0:
        print(get_close_matches(w, data.keys())[0])
        return dictionarry(get_close_matches(w, data.keys())[0])
    else:
        return "The word doesn't exist. Please double check it."


def speak():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
                return r.recognize_google(audio)
        except:
                n = "Could not understand audio, Try it typing!"
                spee('I didnt get that. try it typing.')
                return n

def listToString(s):  
    str1 = ""   
    for ele in s:  
        str1 += ele   
    return str1  

def search_for_n(n):
        if n == "open calc" or n == "open calculator" or n == "open calci":
                spee("opening calculator in new window....")
                q = "opening calculator in new window...."
                calcul()
                return q
        
        

        elif n == "rec my face" or n == "open camera" or n == "can you see me":
                spee("opening camera\nif you want to exit camera press q on your keybord")
                q = face_rec_main()
                count = len(q)
                q = listToString(q)
                        
                print(q)
                q = f"A total of {count} people have arived in meeting\nThey are: {q}"
                return q

        elif n == 'record for the meeting' in n:
                start()
                conv()
        elif 'search for' in n:
                n = n.replace('search for ', '')
                q = search(n)
                return q
        elif 'navigate to' in n:
                b = n.replace('navigate to', '')
                q = navigate(b)
                return q
        elif "tell me the meaning of" in n:
                n = n.replace("tell me the meaning of ","")
                q = dictionarry(n)
                return q
        elif "what is the meaning of" in n:
                n = n.replace("tell me the meaning of ","")
                q = dictionarry(n)
                return q
        elif "meaning of" in n:
                n = n.replace("meaning of ","")
                q= dictionarry(n)
                return q
        elif 'tell me about' in n:
                n = n.replace('tell me about ', '')
                q = wikip(n)
                return q
        elif 'navigate me from' in n:
                b = n.replace('navigate me from', '')
                q = navigateing(b)
                return q
        elif 'throw a dice' in n:
                q = throw()
                return q
        elif 'what is the time' in n:
                now = datetime.datetime.now()
                real_time = now.strftime("%I:%M %p")
                return "It's"+real_time
        elif 'what is the date' in n:
                now = datetime.datetime.now()
                real_time = now.strftime("%d-%m-%Y")
                return "today is "+real_time
        elif 'toss a coin' in n:
                q = toss()
                return q

        if 'open player' in n:
                n = n.replace('open ', '')
                spee("opening" + n)
                command = r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
                os.system(command)
                return q


        elif 'open' in n:
                n = n.replace('open ', '')
                q = browser(n)
                return q
        else:
                q = extras_spam(n)
                return q     
class Ui_MainWindow(object):
    def __init__(self):
            self.ab = "!!!"
            self.add = "Vimigos6@gmail.com"
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1244, 872)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #f0e3ff;")

        #end of the code for main window----------------------------------------------------------------------->

        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(1060, 710, 51, 51))
        self.send_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.send_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/enter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_button.setIcon(icon1)
        self.send_button.setIconSize(QtCore.QSize(50, 50))
        self.send_button.setObjectName("send_button")
        self.send_button.setStyleSheet("background-color:#f0e3ff; border-radius: 20px ; border-width: 2px; font-size: 20px;")

        self.send_button.clicked.connect(self.dataUpdater)

        self.mic_input = QtWidgets.QPushButton(self.centralwidget)
        self.mic_input.setGeometry(QtCore.QRect(1160, 710, 51, 51))
        self.mic_input.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mic_input.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mic_input.setIcon(icon2)
        self.mic_input.setIconSize(QtCore.QSize(50, 50))
        self.mic_input.setObjectName("mic_input")
        self.mic_input.setStyleSheet("background-color:#f0e3ff; border-radius: 20px ; border-width: 2px; font-size: 20px;")
        self.mic_input.clicked.connect(self.line_updater)
  
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(270, 30, 701, 61))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setStyleSheet("background-color: #916dd5; border-radius: 20px ; border-width: 2px; font-size: 20px; color:white;")
  
        self.lineEdit_11 = QtWidgets.QTextEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(110, 130, 991, 451))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_11.setStyleSheet("background-color: white; border-radius: 20px ; border-width: 2px; font-size: 25px;")


        self.user_input = QtWidgets.QLineEdit(self.centralwidget)
        self.user_input.setGeometry(QtCore.QRect(90, 700, 911, 61))
        self.user_input.setObjectName("user_input")
        self.user_input.setText("")
        self.user_input.setStyleSheet("background-color: white; border-radius: 20px ; border-width: 2px; font-size: 20px;")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1244, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def line_updater(self):
        spk("Now taking input from your voice so please wait. Now speak.")
        QApplication.processEvents()
        self.lineEdit_11.setText("NOW SPEAK!")
        QApplication.processEvents()
        n = speak()
        QApplication.processEvents()
        if n == "Could not understand audio, Try it typing!":
                self.lineEdit_11.setText(n)
        else:
                self.user_input.setText(n)
        QApplication.processEvents()
    def dataUpdater(self):
        query = self.user_input.text()
        self.lineEdit_8.setText(" "+query)
        n = query
        n = n.lower()

        if self.ab == "on":
                self.lineEdit_11.setText("Sending message, Please wait!")
                spk("Sending message, Please wait")
                self.lineEdit_8.setText("")
                QApplication.processEvents()
                q = send_mail(self.add,n)
                self.lineEdit_11.setText(" "+q)
                self.lineEdit_11.setText(q)
                self.lineEdit_8.setText("")
                QApplication.processEvents()
                spk(q)
                self.ab = "off"
        else:
                if "send email to" in n:
                        n = n.replace("send email to ","")
                        if n =="dhawal" or n == "satya" or n == "utkarsh" or n =="simran" or n =="hemang" or n=="ekansh" :
                                self.add = nametomail(n)
                                q = "What is your message?" 
                                self.lineEdit_11.setText(" "+q)
                                self.ab = "on"
                        else:
                                q = f"Receiver data is not available"
                                self.lineEdit_11.setText(" "+q)
                                QApplication.processEvents()
                                
                                



                else:
                        q = search_for_n(n)
                
                self.lineEdit_11.setText(" "+q)
                self.user_input.setText("")
                QApplication.processEvents()
                spppp(q)
                

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.send_button.setStatusTip(_translate("MainWindow", "To ask bot"))
        self.send_button.setShortcut(_translate("MainWindow", "Return"))
        self.mic_input.setStatusTip(_translate("MainWindow", "Use voice "))
        self.mic_input.setShortcut(_translate("MainWindow", "Ctrl+M"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
