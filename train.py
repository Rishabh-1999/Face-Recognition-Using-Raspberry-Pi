import face_recognition
import picamera
import numpy as np
import os
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

def createFolder(path):
   try:
      if not os.path.exists("dataset/" + path) :
          os.makedirs("dataset/" + path)
   except OSError:
      print("Error: creating directory" + path)

id = [None] * 5
name = [None] * 5
print("Capturing images")
i = 0
while True:
    id[i] = input("Enter the id: ")
    name[i] = input("Enter the name: ")
    createFolder(name[i])
    os.chdir("dataset/" + name[i])
    for j in range(5):
        camera.capture(id[i]  + "-" + str(j)  + ".jpg")
        output = face_recognition.load_image_file(id[i] + "-" + str(j) + ".jpg")
        #new image encoding
        face_encodings = face_recognition.face_encodings(output)
        #checking that a face is there or not
        if len(face_encodings) == 0:
            print("Please show a face")
            continue
    os.chdir("../../")
    i += 1
print(id)
print(name)