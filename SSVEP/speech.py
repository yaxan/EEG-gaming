from importlib_metadata import re
import speech_recognition as sr
import pyttsx3

def get_text_from_speech(recognizer):

    """
    Returns speech based on listening

    :param recognizer: speech_recognition.Recognizer object  
    :return text: text that was listened to
    """

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        # Listen for audio and convert it to text
        audio = recognizer.listen(source, timeout=3)

        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, the computer didn't understand what you said."
        except sr.RequestError as e:
            return "Request error: {e}"

def text_to_speech(engine, str):
    """
    Outputs speech (from speaker) based on input string

    :param engine: pyttsx3 engine object
    :param str: string/text to be said out loud
    """

    engine.say(str)
    engine.runAndWait()

    return

if __name__ == "__main__":
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.7)

    recognizer = sr.Recognizer()

    text_to_speech(engine, "Say something in 3 seconds")
    text = get_text_from_speech(recognizer)
    text_to_speech(engine, "I think you said:")
    text_to_speech(engine, text)
