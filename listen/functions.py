import speech_recognition as sr

from useful.speak import speak_ia


def listen(to_try=3):
    """
    This method uses the 'speech_recognition' package to listen to a client request and convert it to text.

    :param to_try: Used to control the number of times the AI will try to listen to the client.
    :return: Will return the customer's voice in text.
    """

    print(to_try)  # TODO - Kayo: remove print.

    if to_try > 0:
        try:
            recognizer = sr.Recognizer()

            with sr.Microphone() as microphone:
                try:
                    voice = recognizer.listen(microphone, phrase_time_limit=5)
                except Exception as e:
                    raise Exception(f'Error when trying to listen to the client. {str(e)}')

                try:
                    text = recognizer.recognize_google(voice, language='pt-BR').lower()
                except Exception as e:
                    raise Exception(f'Error when trying to convert voice to text using "recognize_google". {str(e)}')

                print(text)  # TODO - Kayo: remove print.

                return text
        except Exception as e:
            print(str(e))  # TODO - Kayo: send exception to admin email or sentry.

            if to_try == 3:
                speak_ia('Não entendi... pode repeti?')  # TODO - Kayo: create vocabulary to communicate.

            else:
                speak_ia('Continuo sem entender... pode repeti?')  # TODO - Kayo: create vocabulary to communicate.

            return listen(to_try - 1)

    speak_ia('Infelizmente eu não entendi o que você disse.')  # TODO - Kayo: create vocabulary to communicate.
