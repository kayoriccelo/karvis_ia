import speech_recognition

from useful.exceptions import ListenClientError, UnderstandAudioError


class ListenBase:
    _speech_recognition = None
    recognizer = None
    microphone = None
    language = None
    phrase_time_limit = None
    recognize_and_interact = None

    def __init__(self, language, recognize_and_interact, phrase_time_limit):
        self.language = language
        self.phrase_time_limit = phrase_time_limit
        self.recognize_and_interact = recognize_and_interact
        self._speech_recognition = speech_recognition
        self.recognizer = self._speech_recognition.Recognizer()

    def convert_voice_in_text(self, voice):
        try:
            voice_text = self.recognizer.recognize_google(voice, language=self.language)

            return voice_text.lower()

        except Exception as e:
            raise UnderstandAudioError(f"Google speech recognition could not understand the audio. {str(e)}")

    def listen_voice(self):
        try:
            with self._speech_recognition.Microphone() as microphone:
                return self.recognizer.listen(microphone, phrase_time_limit=self.phrase_time_limit)

        except Exception as e:
            raise ListenClientError(f'Error when trying to listen to the client. {str(e)}')

    def listen_voice_text(self):
        print('listening...')

        voice = self.listen_voice()

        return self.convert_voice_in_text(voice)
