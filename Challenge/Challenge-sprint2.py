import cv2

classificador = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

imagem = cv2.imread(r'../images/rosto1.jpg')

cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

faces = classificador.detectMultiScale(cinza)

for x, y, l, a in faces:
    imagem = cv2.rectangle(imagem, (x,y), (x+l, y+a), (255, 0, 0), 2)

cv2.imshow("Faces detectadas", imagem)
cv2.waitKey()