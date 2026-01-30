import speech_recognition as sr
from deep_translator import GoogleTranslator

r = sr.Recognizer()
translator = GoogleTranslator(source='en', target='ml')  # English → malayalam

with sr.Microphone() as source:
    print("Please speak...")
    r.adjust_for_ambient_noise(source, duration=1)

    try:
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        text = r.recognize_google(audio, language="en-US")
        print("You said:", text)

        translated = translator.translate(text)
        print("Translated:", translated)

    except sr.UnknownValueError:
        print("I heard something, but could not understand. Please speak clearly.")

    except sr.WaitTimeoutError:
        print("You did not speak in time.")

    except sr.RequestError as e:
        print("Speech service error:", e)

