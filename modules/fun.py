import random
import win32com.client as wincl
dice = ['1', '2', '3', '4', '5', '6']
coin = ['Heads', 'Tails']
speak = wincl.Dispatch("SAPI.SpVoice")
spk = speak.Speak


def toss():
    random.choice(coin)
    spk('You got' )
    return random.choice(coin)


def throw():
    spk('You got' )
    return random.choice(dice)
