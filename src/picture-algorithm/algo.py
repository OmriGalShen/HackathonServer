# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image

import cv2
import numpy as np

print(f"OpenCV Version: {cv2.__version__}")
image = Image.open('test1.jpeg')
new_image = image.resize((400, 400))
new_image.save('1_resized.jpeg')
# ריהוט כלי בית, מוצרי חשמל, טלוויזיות, תכשיטים אומנות
image = Image.open('test1yad2.jpeg')
new_image = image.resize((400, 400))
new_image.save('yad2_resized.jpeg')

img1 = cv2.imread('1_resized.jpeg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('yad2_resized.jpeg', cv2.IMREAD_GRAYSCALE)

# ------------------->OPTION 2<---------------

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)
print(len(matches))
matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:30], None)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('matching result', matching_result)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------------->OPTION 1<---------------
#
# sift = cv2.SIFT_create()
# orb = cv2.ORB_create(nfeatures=2000000)
#
# kp1, des1 = sift.detectAndCompute(img1, None)
# kp2, des2 = sift.detectAndCompute(img2, None)
#
# imgKp1 = cv2.drawKeypoints(img1, kp1, None)
# imgKp2 = cv2.drawKeypoints(img2, kp2, None)
# bf = cv2.BFMatcher()
# matches = bf.knnMatch(des1, des2, k=2)
# good = []
#
# for m, n in matches:
#     if m.distance < 0.80 * n.distance:
#         good.append([m])
#
# img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
#
# # cv2.imshow('Kp1', imgKp1)
# # cv2.imshow('Kp2', imgKp2)
# cv2.imshow('img3', img3)
#
# # cv2.imshow('img1', img1)
# # cv2.imshow('img2', img2)
# cv2.waitKey(0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
