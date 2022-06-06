import cv2
import os
import numpy as np

eigenFace = cv2.face.EigenFaceRecognizer_create()
fisherFace = cv2.face.FisherFaceRecognizer_create()

lbph = cv2.face.LBPHFaceRecognizer_create()

def getImagemPeloNome():
    caminhos = [os.path.join('imagens', f) for f in os.listdir('imagens')]
    faces = []
    nomes = []

    for caminhoImagem in caminhos:
        imagemFace = cv2.imread(caminhoImagem)
        imagemFaceCinza = cv2.cvtColor(imagemFace, cv2.COLOR_BGR2GRAY)

        nome = os.path.split(caminhoImagem)[-1].split('_')[0]
        print(nome)

        if nome == 'claudio':
            nomes.append(1)
        else:
            nomes.append(2)

        faces.append(imagemFaceCinza)
    return np.array(nomes), faces


nomes, faces = getImagemPeloNome()
print(nomes)
eigenFace.train(faces, nomes)
eigenFace.write('classificadorEigen.yml')
