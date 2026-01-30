import pyttsx3
from deep_translator import GoogleTranslator

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Input text
text = input("Enter text: ")

# Translate text
translator = GoogleTranslator(source="en", target="hi")  # English → Hindi
translated_text = translator.translate(text)
print("Translated text:", translated_text)

# Speak translated text
engine.say(translated_text)
engine.runAndWait()
