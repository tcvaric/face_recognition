# -*- coding: utf-8 -*-
"""Face recognition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H3eb9uYJHyyjnkTNQ8Qo2_vw7Qw2Xbrw
"""

!pip install face_recognition

from google.colab import files

files.upload()

ls

import face_recognition
from PIL import Image, ImageDraw

image = face_recognition.load_image_file("face_01.jpg")
face_locations = face_recognition.face_locations(image)
face_locations

image

def face_detection(image, face_locations):
    face_locations = (face_locations[0][1], face_locations[0][0], face_locations[0][3], face_locations[0][2])
    im = Image.fromarray(image)
    draw = ImageDraw.Draw(im)
    draw.rectangle(face_locations, fill=None, outline=(255,0,0), width=5)
    return im

face_detection(image, face_locations)

image1 = face_recognition.load_image_file("face_01.jpg")
image2 = face_recognition.load_image_file("face_02.jpg")

encoding1 = face_recognition.face_encodings(image1)[0]
encoding2 = face_recognition.face_encodings(image2)[0]

Image.fromarray(image1)

Image.fromarray(image2)

face_recognition.compare_faces([encoding1], encoding2, tolerance=0.5)

def landmark_point(xy1, size=5):
  xy2 = xy1[0]+size, xy1[1]+size
  return [(xy1), (xy2)]

image = face_recognition.load_image_file("face_02.jpg")
face_landmark_list = face_recognition.face_landmarks(image)

im = Image.fromarray(image)
draw = ImageDraw.Draw(im)

for face_landmark in face_landmark_list[0]:
    for xy in face_landmark_list[0][face_landmark]:
        draw.ellipse(landmark_point(xy, size=4), outline=(255,0,0), fill=(255,0,0))

im