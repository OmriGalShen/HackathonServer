from PIL import Image

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('kitchen.jpeg')
classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
print(classNames)

net = cv2.dnn.readNet("yolov3-tiny.weights", "yolov3-tiny.cfg")

blob = cv2.dnn.blobFromImage(img, 1 / 255, (320, 320), (0, 0, 0), swapRB=True, crop=False)
blob.shape