import pyttsx3
import speech_recognition as sr
import pyaudio as pa

def get():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"I'm listening... ")
        
        #adjusting mic for background sounds
        r.adjust_for_ambient_noise(source)
        
        #getting data from mic and adding a pause
        audio = r.listen(source, timeout=5)
        print(f"Got you. Analysing...")
        
    try:
        text = r.recognize_google(audio)
        print(f"These are your words:\n {text}")
    
    except Exception as e:
        print("Unexpected error!")
        
get()