from listen.base import ListenBase


class ListenContinuously(ListenBase):
    phrase_time_limit_continuously = None
    stop_listening = False

    def __init__(
        self, language, recognize_and_interact, phrase_time_limit=5, phrase_time_limit_continuously=3
    ):
        super().__init__(language, recognize_and_interact, phrase_time_limit)

        self.phrase_time_limit_continuously = phrase_time_limit_continuously

    def listen_and_recognize(self, recognizer, microphone):
        try:
            voice_text = recognizer.recognize_google(microphone, language=self.language)
            voice_text = voice_text.lower()

            print(voice_text)

            if self.recognize_and_interact:
                self.recognize_and_interact(voice_text)

        except self._speech_recognition.UnknownValueError:
            print("Google speech recognition could not understand the audio")

        except self._speech_recognition.RequestError as e:
            print(f"Unable to request results from Google speech recognition service; {e}")

    def to_stay_listening_continuously(self):
        microphone_background = self._speech_recognition.Microphone()
        recognizer_background = self._speech_recognition.Recognizer()

        with microphone_background as microphone_background_source:
            recognizer_background.adjust_for_ambient_noise(microphone_background_source)

        recognizer_background.listen_in_background(
            microphone_background, self.listen_and_recognize, self.phrase_time_limit_continuously
        )

        self.stop_listening = True

        import time

        while self.stop_listening:
            time.sleep(0.1)
