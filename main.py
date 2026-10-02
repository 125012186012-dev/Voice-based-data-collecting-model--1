import json
import pyttsx3 as ts
import speech_recognition as sr

profile={}

with open("questiondata.json", "r") as file:
    questions = json.load(file)
    
recognizer = sr.Recognizer()

def speak(questionname):
    engine = ts.init()
    question=questions[questionname]
    print(question)
    engine.say(question)
    engine.runAndWait()
    
    with sr.Microphone() as source:
       print("Listening...")
       audio=recognizer.listen(source)
              
    try:
         user_input = recognizer.recognize_google(audio)
         profile[questionname]= user_input
         print("your input :",user_input)
     
    except sr.UnknownValueError:
          print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
          print("Could not request results; {0}".format(e))
 
for q in questions:
    speak(q)


with open("Answersdata.json","w") as file:
    json.dump(profile,file,indent=4) 
    
print("\n Profile saved in the JSON")