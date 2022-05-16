import cv2
import mediapipe as mp
import speech_recognition as sr

#insere na variável webcam o frame retirado na camera padrão
#O parâmetro que o vídeoCapture recebe, é o número da webcam que você deseja usar
webcam = cv2.VideoCapture(0)

#utiliza a solução do media pipe que já está pronta
solucao_reconhecimento_rosto = mp.solutions.face_detection

#Aqui é onde recebe a imagem daquele momento e detecta se há um rosto naquela imagem
reconhecedor_de_rostos = solucao_reconhecimento_rosto.FaceDetection()

#Faz o desenho do rosto capturado
desenho = mp.solutions.drawing_utils

def sexta_feira_escuta():
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("fale:(vindo da func)")

        audio = mic.listen(source)

        try:
            frase = mic.recognize_google(audio, language='pt').lower()
            print("Texto reconhecido: " + frase)

        except sr.UnknownValueError:
            print("Não entendi")
        return frase

'''
    Como é retirado um frame (uma foto) por vêz, é necessário que a gente crie um loop
    infinito para que toda fez que um frame seja tirado, o reconhecedor de rosto
    detecte que há um rosto ali dentro
'''
while True:
    '''Ler as informacoes da webcam
    Webcam.read retorna uma informação booleana caso esteja lendo alguma imagem
    e uma lista do frame tirado no momento
    '''
    verificador, frame = webcam.read()

    #Se o retorno não for um True, o while true é cancelado
    if not verificador:
        break
    #Reconhecer os rostos que tem ali dentro
    lista_rostos = reconhecedor_de_rostos.process(frame)

    #Se detectar algum rosto, é desenhado um quadrado em volta do rosto
    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            #Desenhar os rostos na imagem
            desenho.draw_detection(frame, rosto)
    #Mostra a imagem capturada e os rostos
    cv2.imshow("Rostos na Webcam", frame)

    #Quando apertar ESC, para o Loop
    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()