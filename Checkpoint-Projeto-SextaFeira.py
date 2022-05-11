import pyttsx3
import speech_recognition as sr
import os

sextaFeira = pyttsx3.init()

recon = sr.Recognizer()
comando = ""


def sexta_feira_responde():
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")

        audio = mic.listen(source)

        try:
            frase = mic.recognize_google(audio, language='pt').lower()
            print("Texto reconhecido: " + frase)

        except sr.UnknownValueError:
            print("Não entendi")
        return frase

while True:
    resultado = sexta_feira_responde()

    match
    if resultado == "ola" or resultado == "olá":
        print("o teste de validação funcionou")
    print("passei do if")