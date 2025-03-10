import pyttsx3

engine = pyttsx3.init()
data = input("What should I say: ")
engine.say(data)
engine.runAndWait()