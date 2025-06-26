import os
import random
import uuid

import cv2
import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt


POS_PATH = os.path.join('data', 'positive')
NEG_PATH = os.path.join('data', 'negative')
ANC_PATH = os.path.join('data', 'anchor')

os.makedirs(POS_PATH)
os.makedirs(NEG_PATH)
os.makedirs(ANC_PATH)

def Get_image():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()

        frame = frame[120:370, 200:460]

        key = cv2.waitKey(1) & 0xFF

        if key == ord('\r'):
            imgname = os.path.join(ANC_PATH, '{}.jpg'.format(uuid.uuid1()))
            cv2.imwrite(imgname, frame)

        if key & 0xFF == ord('s'):
            imgname = os.path.join(POS_PATH, '{}.jpg'.format(uuid.uuid1()))
            cv2.imwrite(imgname, frame)
            
        cv2.imshow('frame', frame)
        
        if key & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()       

