from PIL import Image

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('IDC_kitchen1.jpeg.jpeg')
classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
print(classNames)

cfg_path = "yolov3.weights"
weights_path = "yolov3.cfg"

net = cv2.dnn.readNet(cfg_path, weights_path)
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0,255,size=(len(classNames),3))

img = cv2.imread('IDC_kitchen1.jpeg')
cv2.resize(img, None, fx=0.7, fy=0.7)

height, width, channels = img.shape

# Detecting object
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0.0, 0), swapRB=True, crop=False)
# for b in blob:
#     for n, img_blob in enumerate(b):
#         cv2.imshow(str(n), img_blob)

net.setInput(blob)
outs = net.forward(output_layers)

class_ids = []
confidences = []
boxes = []

# Showing information to the screen
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:  # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Recntangle coordinates
            x = int(center_x - w / 2)
            y = int(center_y - w / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)
#indexes = cv2.dnn
# number_object_detected = len(boxes)  # numbers of detected objects


indexes = cv2.dnn.NMSBoxes(boxes,confidences, 0.5, 0.4)
print(indexes)

font = cv2.FONT_HERSHEY_PLAIN
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = classNames[class_ids[i]]
        color = colors[i]
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x, y + 30), font, 3, color, 3)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
