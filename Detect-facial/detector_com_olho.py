import cv2
classificadorFace = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
classificadorOlho = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

imagem = cv2.imread(r'images\angelina.jpeg')

cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = classificadorFace.detectMultiScale(cinza)
olhos = classificadorOlho.detectMultiScale(cinza, scaleFactor=8)


for x, y, l, a in faces:
    imagem = cv2.rectangle(imagem, (x, y), (x+l, y+a), (255, 0, 0), 2)

for x, y, l, a in olhos:
    imagem = cv2.rectangle(imagem, (x, y), (x+l, y+a), (0, 0, 255), 2)

cv2.imshow("Faces detectadas", imagem)
cv2.waitKey()
