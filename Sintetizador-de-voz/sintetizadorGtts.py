from gtts import gTTS
from pygame import mixer
#import os

voz = gTTS("Olá mundo", lang='pt', tld='com.br')
voz.save('C:/Users/logonrmlocal/Desktop/audio.mp3')

mixer.init()
mixer.music.load("C:/Users/logonrmlocal/Desktop/audio.mp3")
mixer.music.play()


#Outra forma de executar
#os.system('C:/Users/logonrmlocal/Desktop/audio.mp3')