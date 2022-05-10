import speech_recognition as sr


recon = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        print("Quais valores deseja Multiplicar?")
        audio = recon.listen(source)

        contaxt = recon.recognize_google(audio, language='pt')
        if contaxt == "fechar":
            break
        print(contaxt)
        print("Resultado: ", str(int(contaxt[0]) * int(contaxt[4])))
