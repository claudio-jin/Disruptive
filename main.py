import pyttsx3

en = pyttsx3.init()

#en.setProperty('voice', b'brasil')
en.setProperty('volume', 1)

rate = 155
i = 0

while i < 10:
    en.setProperty('rate', rate)
    msg = "créu"
    en.say(msg)
    en.runAndWait()
    rate += 100
    i += 1
    print(i)
