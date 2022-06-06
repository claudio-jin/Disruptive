import cv2

detectorFace = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
reconhecedor = cv2.face.EigenFaceRecognizer_create()

reconhecedor.read('classificadorEigen.yml')

largura, altura = 220, 220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
camera = cv2.VideoCapture(0)

while True:
    status, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30, 30))

    try:
        for x, y, largura, altura in facesDetectadas:
            imagemFace = cv2.resize(imagemCinza[x: x + largura, y: y + altura], (largura, altura))
            cv2.rectangle(imagem, (x, y), (x + largura, y + altura), (0, 0, 255), 2)
            nome, confianca = reconhecedor.predict(imagemFace)
            print(confianca)
            if nome == 1:
                nome = 'Claudio'
            cv2.putText(imagem, str(nome), (x, y + altura + 50), font, 2, (0, 0, 255))

    except:
        print("bug")
    cv2.imshow("face", imagem)
    if cv2.waitKey(1) == ord('q'):
        break
    cv2.waitKey(1)
