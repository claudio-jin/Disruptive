import speech_recognition as sr

recon = sr.Recognizer()

PATH = "D:/Audio/WhatsApp Ptt 2022-05-03 at 11.34.23.wav"

with sr.AudioFile(PATH) as source:
    audio = recon.record(source)
    frase = recon.recognize_google(audio, language='pt')
    calcular = frase.split()
    if calcular[1] == 'x':
        print(int(calcular[0]) * int(calcular[2]))
    elif calcular[1] == '+':
        print(int(calcular[0]) + int(calcular[2]))
    elif calcular[1] == '-':
        print(int(calcular[0]) - int(calcular[2]))
    else:
        print(int(calcular[0]) / int(calcular[2]))