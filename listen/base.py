import speech_recognition


class ListenBase:
    _speech_recognition = None
    recognizer = None
    microphone = None
    language = None
    recognize_and_interact = None

    def __init__(self, language, recognize_and_interact):
        self.language = language
        self.recognize_and_interact = recognize_and_interact
        self._speech_recognition = speech_recognition
        self.recognizer = self._speech_recognition.Recognizer()
