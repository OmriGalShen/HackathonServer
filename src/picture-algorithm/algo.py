# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image

import cv2
import numpy as np

from database.Repository import repo


def find_num_of_matches(index):
    database_image = Image.open('{}.jpeg'.format(index))
    new_database_image = database_image.resize((500, 500))
    new_database_image.save('database_image.jpeg')
    img1 = cv2.imread('database_image.jpeg', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('client_image.jpeg', cv2.IMREAD_GRAYSCALE)

    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    return len(matches)


def find_best_match():
    max_index = 1
    for index in range(last_index):
        if find_num_of_matches(index) > find_num_of_matches(last_index):
            max_index = index
    return max_index

def price_and_model(picutre_string)
    client_image = Image.open(picutre_string)  # This is the picture from the Client
    new_image = client_image.resize((500, 500))
    new_image.save('client_image.jpeg')
    last_index = repo.lastindex()
    best_match = find_best_match()
    l

print(f"OpenCV Version: {cv2.__version__}")

client_image = Image.open('yad2.jpeg')  # This is the picture from the Client
new_image = client_image.resize((500, 500))
new_image.save('client_image.jpeg')
last_index = repo.lastindex()
best_match = find_best_match()  # our best match - returning the "id" of the pic


# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('matching result', matching_result) # cv2.waitKey(3500)
# ריהוט כלי בית, מוצרי חשמל, טלוויזיות, תכשיטים אומנות
# image = Image.open('test1yad2.jpeg')
# new_image = image.resize((400, 400))
# new_image.save('yad2_resized.jpeg')
# לצלפ קבלה, הערכה של סוקר, תכשיטן שמעריך מעצמו, דו״ח סוקר קודם.


# ------------------->OPTION 2<---------------

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
