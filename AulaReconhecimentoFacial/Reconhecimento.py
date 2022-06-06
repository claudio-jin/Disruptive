import cv2

detectorFace = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalFace_default.xml")
reconhecedor = cv2.face.EigenFaceRecognizer_create()
reconhecedor.read('classificadoreigen.yml')

largura, altura = 220, 220

font = cv2.QT_FONT_NORMAL
camera = cv2.VideoCapture(0)
fim = False

while not fim:
    status, imagem = camera.read()

    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30,30))
    try:
