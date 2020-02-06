from wikipedia import *
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
spk=speak.Speak


#normal wiki command
def wikip(n):
    try:
        q=wikipedia.summary(n, sentences=4)
        return q
    except:
        return "please check your net connection"


