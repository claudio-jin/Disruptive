import cv2
import numpy as np

classificador = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture(0)

amostra = 1
numeroMaxAmostras = 25

nome = input("Digite seu nome: ")
altura, largura = 220, 220

while True:
    status, imagem = camera.read()

    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150, 150))

    for (x, y, altura, largura) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x+largura, y+altura), (0,0,255), 2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Média: ", np.average(imagemCinza))

            if np.average(imagemCinza) > 110:
                imagemFace = cv2.resize(imagemCinza[y: y+altura], (largura, altura))

                localFoto = "imagens/"+str(nome)+"_"+str(amostra)+".jpg"

                cv2.imwrite(localFoto, imagemFace)
                amostra += 1

    cv2.imshow("Face detectada", imagem)
    if amostra > numeroMaxAmostras:
        break

print("Fotos capturadas com sucesso")
camera.release()
cv2.destroyAllWindows()
