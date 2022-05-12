import os
from pygame import mixer
from gtts import gTTS

caminho = input("Digite o caminho em que se encontra o arquivo de texto: ")

teste = os.path.isfile(caminho)

if teste == True:
    with open(caminho) as arquivo:
        print("Carregando arquivo...")
        textinho = arquivo.read()
        print("Inicializando o sintetizador...")
        voz = gTTS(textinho, lang = 'pt')
        print("Gerando a voz... aguarde...")
        voz.save("C:/Users/logonrmlocal/Desktop/texto.mp3")
        mixer.init()
        mixer.music.load("C:/Users/logonrmlocal/Desktop/texto.mp3")
        mixer.music.play()
        input("Falando... Digite o ENETER para finalizar")
else:
    print("Não foi possivel abrir o arquivo")
