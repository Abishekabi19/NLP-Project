import pyttsx3 # requred import 
# initialize engine
engine=pyttsx3.init()
# input text
text=input('enter text:')
# speak text 
engine.say(text)
engine.runAndWait()