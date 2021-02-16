import speech_recognition as sr

class SpeechTranslation:

    r = sr.Recognizer()
    m = sr.Microphone()

    def __init__(self):
        pass

    def listen(self):
        with self.m as source:
            audio = self.r.listen(source)
        return audio

    def translate(self):
        return self.r.recognize_google(audio)
