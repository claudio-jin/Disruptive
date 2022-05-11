import speech_recognition as sr


def ouvir_micro():
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")

        audio = mic.listen(source)

        try:
            frase = mic.recognize_google(audio, language='pt')
            print("texto: " + frase)

        except sr.UnknownValueError:
            print("nao entendi")
        return frase


ouvir_micro()
