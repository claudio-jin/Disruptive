import cv2
classificadorFace = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

imagem = cv2.imread(r'../images/rosto1.jpg')

# converter os pixel da imagem de rgb para preto e branco
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# faces retorna uma tupla
#
faces = classificadorFace.detectMultiScale(cinza)
#minSize é um parametro que coloca como limite um minimo de pixel para detectar
#scaleFactor aumenta a escala das imagens para melhorar a precisao


for x, y, l, a in faces:
    imagem = cv2.rectangle(imagem, (x,y), (x+l, y+a), (255,0,0),2 )
    #primeiro seta a imagem, segundo seta as coord iniciais,
    #terceiro seta a coord inicial mais a largura chegando ao ponto final
    #quarto seta a cor das bordas padrao bgr

cv2.imshow("Faces detectadas",imagem)
cv2.waitKey()
