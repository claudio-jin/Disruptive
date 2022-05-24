import cv2
import os
import numpy as np

eigen = cv2.face.EigenFaceRecognizer_create()

def getImagemPeloNome():
    caminhos =[os.path.join('fotos', f) for f in os.listdir('fotos')]
    print(caminhos)
    faces = []