import pyttsx3
import speech_recognition as sr
import os

print("Olá, deseja ouvir uma música?")
robo = pyttsx3.init()
robo.say("Olá, deseja ouvir uma música?")
robo.setProperty('voice', b'brasil')
robo.setProperty('rate', 140)
robo.setProperty('volume', 1)
robo.runAndWait()

recon = sr.Recognizer()
resposta = ""

with sr.Microphone() as source:
    while True:
        audio = recon.listen(source)
        resposta = recon.recognize_google(audio, language='pt')
        print("Texto reconhecido: ", resposta)
        if resposta == "sim":
            robo.setProperty('rate', 180)
            robo.setProperty('volume', 1)
            robo.setProperty('voice', b'brasil')
            robo.say("Ok, abrindo mídia")
            robo.runAndWait()
            os.system("caminho da musica")
        elif resposta == "não":
            robo.setProperty('rate', 180)
            robo.setProperty('volume', 1)
            robo.setProperty('voice', b'brasil')
            robo.say("Ok, encerrando programa")
            robo.runAndWait()
            break
