import speech_recognition as sr

from speak.background import speak_ai


def listen(try_times=3):
    """
    Uses the 'speech_recognition' package to listen to a client request and convert it to text.

    :param try_times: Used to control the number of times the AI will try to listen to the client.
    :return: Will return the customer's voice in text.
    """

    print(f'to try: {try_times}')  # TODO - Kayo: remove print.

    if try_times > 0:
        try:
            recognizer = sr.Recognizer()

            with sr.Microphone() as microphone:
                try:
                    voice = recognizer.listen(microphone, phrase_time_limit=5)  # TODO - Kayo: configuration phrase_time_limit in AI.
                except Exception as e:
                    raise Exception(f'Error when trying to listen to the client. {str(e)}')

                try:
                    text = recognizer.recognize_google(voice, language='pt-BR').lower() # TODO - Kayo: configuration language in AI.
                except Exception as e:
                    raise Exception(f'Error when trying to convert voice to text using "recognize_google". {str(e)}')

                print(text)  # TODO - Kayo: remove print.
                speak_ai(text)  # TODO - Kayo: remove speak test.

                return text
        except Exception as e:
            print(str(e))  # TODO - Kayo: send exception to admin email or sentry.

            new_try_times = try_times - 1

            if new_try_times == 2:
                speak_ai('Não entendi... pode repeti?')  # TODO - Kayo: create vocabulary to communicate.

            else:
                speak_ai('Continuo sem entender... pode repeti?')  # TODO - Kayo: create vocabulary to communicate.

            return listen(new_try_times)

    speak_ai('Infelizmente eu não entendi o que você disse.')  # TODO - Kayo: create vocabulary to communicate.
