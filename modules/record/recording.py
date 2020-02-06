import sounddevice as sd
from scipy.io.wavfile import write
import os
import speech_recognition as sr
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
spk = speak.Speak

def start():
    fs = 44100  # this is the frequency sampling; also: 4999, 64000
    seconds = 10  # Duration of recording
    
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    spk("Recording Started.")
    sd.wait()  # Wait until recording is finished
    write(r'database\output.wav', fs, myrecording)  # Save as WAV file
    os.startfile(r"database\output.wav")
