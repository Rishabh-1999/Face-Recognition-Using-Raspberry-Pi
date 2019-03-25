import face_recognition
import picamera
import numpy as np
import os
import pymysql
import sys
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

#cre for rds instance

REGION = 'us-east-1'

rds_host  = "epics.cchqlmtm8iyr.us-east-1.rds.amazonaws.com"
name = "Rishabh"
password = "chitkara"
db_name = "epics"

def save_data(data):
    """
    This function fetches content from mysql RDS instance
    """
    result = []
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""insert into studentDetails (id, name) values( %s, '%s')""" % (data['id'], data['name']))
        cur.execute("""select * from studentDetails""")
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print ("Data from RDS...")
        print (result)


def createFolder(path):
   try:
      if not os.path.exists("dataset/" + path) :
          os.makedirs("dataset/" + path)
   except OSError:
      print("Error: creating directory" + path)

#intializing the empty dict for student data
data = {}
print("Capturing images")
i = 0
while True:
    data["id"] = input("Enter the id: ")
    data["name"] = input("Enter the name: ")
    createFolder(data["name"])
    os.chdir("dataset/" + data["name"])
    for j in range(5):
        camera.capture(data["id"]  + "-" + str(j)  + ".jpg")
        output = face_recognition.load_image_file(data["id"] + "-" + str(j) + ".jpg")
        #new image encoding
        face_encodings = face_recognition.face_encodings(output)
        #checking that a face is there or not
        if len(face_encodings) == 0:
            print("Please show a face")
            continue
    os.chdir("../../")
    #saving data to the database
    save_data(data)
    i += 1