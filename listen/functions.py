import speech_recognition as sr


# ouvir
def listen(to_try=3):  # tentar
    if to_try > 0:
        try:
            # reconhecedor
            recognizer = sr.Recognizer()

            # microfone
            with sr.Microphone() as microphone:
                # voz
                voice = recognizer.listen(microphone, phrase_time_limit=5)

                # texto
                text = recognizer.recognize_google(voice, language='pt-BR').lower()

                print(text)

                return
        except Exception as e:
            print(str(e))

            return listen(to_try - 1)

    if to_try > 0:
        print("I can't hear anything")
        print('não consigo ouvir nada')
