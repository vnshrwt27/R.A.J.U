import pyttsx3
import pyaudio
import webbrowser
import wikipedia
import datetime
import speech_recognition as sr



engine=pyttsx3.init('sapi5')
voicespeed=160
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',voicespeed)
def speak(string):
    engine.say(string)
    engine.runAndWait()
def take():
    r=sr.Recognizer()
    with sr.Microphone(device_index=None) as source:
        r.pause_threshold=1
        print('....')
        audio=r.listen(source)
    
    
    try:
        print('....')
        query=r.recognize_google(audio,language='en-in')
        print(f'user said {query}\n')
        
        

    except Exception as e:
        print(e)
        print('say that again')
        return"None"
    
    
    return query
def CheckCommand(query):
    if query=='jine mera dil luteya':
        speak('oh ho')

    if 'wikipedia' in query:
        pass

    
        
    
if __name__ == "__main__":
    query=take().lower()
    CheckCommand(query)
   
    