import speech_recognition as sr

def conv():
    r = sr.Recognizer()
    with sr.AudioFile(r'database\SteveJobsSpeech_2min.wav') as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            file=open(r"database\output1.txt","w")
            file.write(text)
        except:
            return 'Sorry.. run again...'
