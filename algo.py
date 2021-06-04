# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os

from PIL import Image

import cv2
import numpy as np
import sys

from database.Repository import repo

# print(f"OpenCV Version: {cv2.__version__}")


def find_num_of_matches(index):
    print("path:"+os.path.relpath(__file__))
    database_image = Image.open('database/images/{}.jpeg'.format(index))
    # database_image = Image.open('database/images/{}.jpeg'.format(index))
    new_database_image = database_image.resize((400, 400))
    new_database_image.save('database_image.jpeg')
    img1 = cv2.imread('database_image.jpeg', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('client_image.jpeg', cv2.IMREAD_GRAYSCALE)

    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    print(len(matches))
    matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:30], None)
    # cv2.imshow('matching result', matching_result)
    # cv2.waitKey(2000)
    # cv2.destroyAllWindows()

    return len(matches)


def find_best_match():
    max_index = 1
    max_matches = 0
    for index in range(1, last_index + 1):
        print("{} the index is " + format(index))
        curr_matches = find_num_of_matches(index)
        if curr_matches > max_matches:
            max_index = index
            max_matches = curr_matches
    return max_index


last_index = repo.lastindex()


def price_and_model():
    picture_from_app = '5$.jpg'
    client_image = Image.open(picture_from_app)  # This is the picture from the Client
    new_image = client_image.resize((400, 400))
    new_image.save('client_image.jpeg')
    best_match = find_best_match()
    price = repo.getprice(best_match)
    model = repo.getmodel(best_match)
    return f'{model},{model},{price}'


# print(price_and_model())
#
# client_image = Image.open('yad2.jpeg')  # This is the picture from the Client
# new_image = client_image.resize((500, 500))
# new_image.save('client_image.jpeg')

# our best match - returning the "id" of the pic


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
