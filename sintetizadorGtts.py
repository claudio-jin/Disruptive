from gtts import gTTS
from pygame import mixer

voz = gTTS("Olá mundo", lang='pt')
voz.save('C:/Users/logonrmlocal/Desktop/audio.mp3')

mixer.init()
mixer.music.load("C:/Users/logonrmlocal/Desktop/audio.mp3")
mixer.music.play()
