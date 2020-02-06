import webbrowser
import win32com.client as wincl
speak=wincl.Dispatch("SAPI.SpVoice")
spk=speak.Speak

def browser(query):
    try:
        spk("Opening"+query)
        webbrowser.open('www.'+query+'.com')
        return "Opening Browser"
    except:
        
        return "Please check your Internet connection!"
def search(query):
    try:
        spk("Searching for"+query)
        webbrowser.open_new('www.google.com/search?q=' + query)
        return "Searching in Browser"
    except:
        spk("Please check your Internet connection.")
        return "Please check your Internet connection!"
def navigate(query):
    try:
        spk("navigating to" + query)
        webbrowser.open_new('www.google.com/search?q=navigate+to+' + query)
        return "Okay!"
    except:
        spk("Please check your Internet connection.")
        return "Please check your Internet connection!"
def navigateing(query):
    try:
        spk("navigating from" + query)
        webbrowser.open_new('www.google.com/search?q=' + query)
        return "Okay!"
    except:
        spk("Please check your Internet connection.")
        return "Please check your Internet connection!"