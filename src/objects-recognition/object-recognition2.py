import cv2

img = cv2.imread('kitchen.jpeg')

classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtext'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320,320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)
# net.setInputCrop(False)


classIDs, confs, bbox = net.detect(img, confThreshold=0.5)
print(classIDs, bbox)
#
# for classIds, confidence, box in zip(classIDs.flatten(), confs.flatten(), bbox):
#     cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
#
cv2.imshow("output", img)
cv2.waitKey(0)
#
cv2.destroyAllWindows()
