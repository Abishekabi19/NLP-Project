import speech_recognition as sr
from transformers import pipeline


def recognize_and_correct_speech():
    recognizer = sr.Recognizer()

    # Meaning-based correction model
    
    corrector = pipeline(
        "text2text-generation",
        model="vennify/t5-base-grammar-correction"
    )

    try:
        with sr.Microphone() as source:
            print("\nPlease speak...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)

        # Speech to text
        text = recognizer.recognize_google(audio)
        print("\nYou said:")
        print(text)

        # Meaning-based correction
        result = corrector(text, max_length=64)
        corrected_text = result[0]["generated_text"]

        print("\ncorrected sentence:")
        print(corrected_text)

    except sr.WaitTimeoutError:
        print("⏰ You did not speak in time.")

    except sr.UnknownValueError:
        print("❌ Could not understand your speech.")

    except OSError:
        print("🎤 Microphone not detected.")


if __name__ == "__main__":
    recognize_and_correct_speech()





