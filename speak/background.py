import os


def _creating_file_audio_speak(speak_text, file_name='speak_audio_ai', file_format='mp3', language='pt'):
    """
    Used to create file with AI speech. using the package gTTS to convert 'speak_text' in audio.

    :param speak_text: Contains AI speech in text.
    :param file_name: Contains the file name, used when saving the file.
    :param file_format: Contains the file format, used when saving the file.
    :param language: Contains the language used to create the AI dubbed audio.
    :return: Will return path and file name with AI audio format.
    """

    try:
        from gtts import gTTS

        tts = gTTS(text=speak_text, lang=language, slow=False)
        tts.save(f'{file_name}.{file_format}')

        path_name = os.path.dirname(os.path.abspath(f'{file_name}.{file_format}'))

        return path_name, f'{file_name}.{file_format}'
    except Exception as e:
        print(str(e))  # TODO - Kayo: send exception to admin email or sentry.


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

    try:
        import audiosegment as AudioSegment

        path_file_name_format = f'{path_name_origin}/{file_name}.{file_format}'

        audio = AudioSegment.from_file(f'{path_name_origin}/{file_name_format_origin}')
        audio.frame_rate = 26500  # TODO - Kayo: configuration fram_rate in AI.
        audio.export(path_file_name_format, format=file_format)

        os.remove(f'{path_name_origin}/{file_name_format_origin}')

        return path_file_name_format
    except Exception as e:
        print(str(e))  # TODO - Kayo: send exception to admin email or sentry.


def _play_audio_ai(path_file_name_format):
    """
    Used to play AI audio.

    :param path_file_name_format: Contains the file used to play the AI audio.
    """

    try:
        from playsound import playsound

        playsound(path_file_name_format)

        os.remove(path_file_name_format)
    except Exception as e:
        print(str(e))  # TODO - Kayo: send exception to admin email or sentry.


def speak_ai(speak_text=None):
    """
    Used for IA to speak with 'speak_text'.

    :param speak_text: Contains text used for the AI to speak.
    """

    try:
        if not speak_text:
            raise Exception('Text not provided.')

        path_name, file_name_format = _creating_file_audio_speak(speak_text)

        path_file_name_format = _applicate_frame_rate_audio(path_name, file_name_format)

        _play_audio_ai(path_file_name_format)
    except Exception as e:
        print(e)  # TODO - Kayo: send exception to admin email or sentry.
