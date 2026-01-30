import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Please speak...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

            text = recognizer.recognize_google(audio)
            print("You said:", text)

    except sr.WaitTimeoutError:
        print("You did not speak within the time limit. Please try again.")

    except sr.UnknownValueError:
        print("I heard something, but could not understand. Please speak clearly.")

    except sr.RequestError as e:
        print("Could not reach the speech recognition service:", e)

    except OSError:
        print("Microphone not found or not accessible.")

if __name__ == "__main__":
    recognize_speech()
