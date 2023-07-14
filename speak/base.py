import os

from data.vocabulary.choices import (
    TYPE_VOCABULARY_OFFER_HELP, TYPE_VOCABULARY_DID_NOT_UNDERSTAND_WHAT_YOU_SAID,
    TYPE_VOCABULARY_I_DONT_UNDERSTAND_TALKING_AGAIN, TYPE_VOCABULARY_ANYTHING_ELSE,
    TYPE_VOCABULARY_WHAT_INFORMATION_WANT, TYPE_VOCABULARY_I_STILL_DONT_UNDERSTAND_REPEAT,
    TYPE_VOCABULARY_WANT_ADD_NEW_INTENT, TYPE_VOCABULARY_WHAT_INTENT_YOU_WANT_CREATE,
    TYPE_VOCABULARY_WANT_YOU_WANT_SEARCH_CHATGPT, TYPE_VOCABULARY_HOW_MANY_MINUTES_INFORM_KNOWLEDGE,
    TYPE_VOCABULARY_WHAT_INFORM_KNOWLEDGE, TYPE_VOCABULARY_WHAT_KNOWLEDGE_WANT_TEACH,
    TYPE_VOCABULARY_THANKS_FOR_THE_NEW_KNOWLEDGE, TYPE_VOCABULARY_I_FOUND_THE_FOLLOWING_INFORMATION,
    TYPE_VOCABULARY_CONFIRMS_THIS_INFORMATION_FOR_KNOWLEDGE, TYPE_VOCABULARY_WANT_INFORM_KNOWLEDGE,
    TYPE_VOCABULARY_INTRODUCE_YOURSELF
)
from data.vocabulary.methods import try_get_vocabulary
from useful.exceptions import SpeakSayError


class Speak:
    language = None
    frame_rate = 26500

    def __init__(self, language, frame_rate=None):
        self.language = language

        if frame_rate:
            self.frame_rate = frame_rate

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

    def _applicate_frame_rate_audio(
        self, path_name_origin, file_name_format_origin, file_name='speak_audio_from_rate_ai', file_format='mp3'
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
        audio.frame_rate = self.frame_rate
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

    def _say_vocabulary(self, type_vocabulary):
        vocabulary = try_get_vocabulary(type_vocabulary)  # TODO - Kayo: get vocabulary from learn.

        self.say(vocabulary.description)

        return vocabulary

    def say_offer_help(self):
        return self._say_vocabulary(TYPE_VOCABULARY_OFFER_HELP)

    def say_did_not_understand_what_you_said(self):
        return self._say_vocabulary(TYPE_VOCABULARY_DID_NOT_UNDERSTAND_WHAT_YOU_SAID)

    def say_i_dont_understand_talking_again(self):
        return self._say_vocabulary(TYPE_VOCABULARY_I_DONT_UNDERSTAND_TALKING_AGAIN)

    def say_i_still_dont_understand_repeat(self):
        return self._say_vocabulary(TYPE_VOCABULARY_I_STILL_DONT_UNDERSTAND_REPEAT)

    def say_anything_else(self):
        return self._say_vocabulary(TYPE_VOCABULARY_ANYTHING_ELSE)

    def say_what_information_want(self):
        return self._say_vocabulary(TYPE_VOCABULARY_WHAT_INFORMATION_WANT)

    def say_vocabulary_what_inform_knowledge(self):
        return self._say_vocabulary(TYPE_VOCABULARY_WHAT_INFORM_KNOWLEDGE)

    def say_what_intent_yout_want_create(self):
        return self._say_vocabulary(TYPE_VOCABULARY_WHAT_INTENT_YOU_WANT_CREATE)

    def say_want_add_new_intent(self):
        return self._say_vocabulary(TYPE_VOCABULARY_WANT_ADD_NEW_INTENT)

    def say_want_inform_knowledge(self):
        return self._say_vocabulary(TYPE_VOCABULARY_WANT_INFORM_KNOWLEDGE)

    def say_how_many_minutes_inform_knowledge(self):
        return self._say_vocabulary(TYPE_VOCABULARY_HOW_MANY_MINUTES_INFORM_KNOWLEDGE)

    def say_what_you_want_search_chatgpt(self):
        return self._say_vocabulary(TYPE_VOCABULARY_WANT_YOU_WANT_SEARCH_CHATGPT)

    def say_what_knowledge_want_teach(self):
        return self._say_vocabulary(TYPE_VOCABULARY_WHAT_KNOWLEDGE_WANT_TEACH)

    def say_thanks_for_the_new_knowledge(self):
        return self._say_vocabulary(TYPE_VOCABULARY_THANKS_FOR_THE_NEW_KNOWLEDGE)

    def say_i_found_the_following_information(self):
        return self._say_vocabulary(TYPE_VOCABULARY_I_FOUND_THE_FOLLOWING_INFORMATION)

    def say_confirms_this_information_for_knowledge(self):
        return self._say_vocabulary(TYPE_VOCABULARY_CONFIRMS_THIS_INFORMATION_FOR_KNOWLEDGE)

    def say_introduce_yourself(self):
        return self._say_vocabulary(TYPE_VOCABULARY_INTRODUCE_YOURSELF)
