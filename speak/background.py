import os

from useful.exceptions import SpeakSayError


class SpeakBackground:
    language = None

    def __init__(self, language):
        self.language = language

    def _creating_file_audio_speak(self, speak_text, file_name='speak_audio_ai', file_format='mp3'):
        """
        Used to create file with AI speech. using the package gTTS to convert 'speak_text' in audio.

        :param speak_text: Contains AI speech in text.
        :param file_name: Contains the file name, used when saving the file.
        :param file_format: Contains the file format, used when saving the file.
        :return: Will return path and file name with AI audio format.
        """

        from gtts import gTTS

        tts = gTTS(text=speak_text, lang=self.language, slow=False)
        tts.save(f'{file_name}.{file_format}')

        path_name = os.path.dirname(os.path.abspath(f'{file_name}.{file_format}'))

        return path_name, f'{file_name}.{file_format}'

    @staticmethod
    def _applicate_frame_rate_audio(
        path_name_origin, file_name_format_origin, file_name='speak_audio_from_rate_ai', file_format='mp3'
    ):
        """
        Used to apply frame rate to audio. to work it is necessary to install 'apt install -y ffmpeg'.

        :param path_name_origin: Contains the original audio file path.
        :param file_name_format_origin: Contains the original audio file format.
        :param file_name: Contains the new audio file name that will be created.
        :param file_format: Contains the new audio file format that will be created.
        :return: Will return the complete AI audio file with the applied frame rate.
        """

        import audiosegment as AudioSegment

        path_file_name_format = f'{path_name_origin}/{file_name}.{file_format}'

        audio = AudioSegment.from_file(f'{path_name_origin}/{file_name_format_origin}')
        audio.frame_rate = 26500  # TODO - Kayo: configuration fram_rate in AI.
        audio.export(path_file_name_format, format=file_format)

        os.remove(f'{path_name_origin}/{file_name_format_origin}')

        return path_file_name_format

    @staticmethod
    def _play_audio_ai(path_file_name_format):
        """
        Used to play AI audio.

        :param path_file_name_format: Contains the file used to play the AI audio.
        """

        from playsound import playsound

        playsound(path_file_name_format)

        os.remove(path_file_name_format)

    def say(self, speak_text):
        try:
            path_name, file_name_format = self._creating_file_audio_speak(speak_text)

            path_file_name_format = self._applicate_frame_rate_audio(path_name, file_name_format)

            self._play_audio_ai(path_file_name_format)

        except Exception as e:
            SpeakSayError(f"I can not say. {str(e)}")
