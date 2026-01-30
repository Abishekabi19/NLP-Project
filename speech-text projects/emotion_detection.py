import speech_recognition as sr
from transformers import pipeline

# Initialize emotion detection pipeline
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def recognize_emotion():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Please speak...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=7
            )

            # Speech to text
            text = recognizer.recognize_google(audio)
            print("You said:", text)

            # Emotion detection
            results = emotion_classifier(text)[0]  # list of dicts
            detected = {r['label']: round(r['score'], 2) for r in results if r['score'] > 0.2}

            if detected:
                print("Detected emotion(s):", detected)
            else:
                print("No strong emotion detected. Neutral 😐")

    except sr.WaitTimeoutError:
        print("You did not speak within the time limit. Please try again.")

    except sr.UnknownValueError:
        print("I heard something, but could not understand. Please speak clearly.")

    except sr.RequestError as e:
        print("Could not reach the speech recognition service:", e)

    except OSError:
        print("Microphone not found or not accessible.")

if __name__ == "__main__":
    recognize_emotion()
