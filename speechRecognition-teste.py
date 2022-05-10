import speech_recognition as sr

recon = sr.Recognizer()

with sr.Microphone() as source:
    recon.adjust_for_ambient_noise(source, duration=3)
    while True:
        print("Fale algo..")
        audio = recon.listen(source)
        print("Reconhecendo...")
        print(recon.recognize_sphinx(audio))