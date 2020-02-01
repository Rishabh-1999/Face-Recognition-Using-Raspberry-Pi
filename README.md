# Face-Recognition-Using-Raspberry-Pi
Face Recognition System using Raspberry Pi for Marking attendance.

Libaray used
----------------------
- CMAKE module
- face_recognition  module
- numpy module
- os module
- pymysql module
- sys module
- imutils module
- Amazon Relational Database module

Project Architecture
--------------------
It is diveded into three parts
1. Raspberry Pi
2. Android App
3. AWS EC2 Instances

Work
-----
- This module recognize faces stored in memory by making *encoding* in xml format of each person/student and after recognizing person/student, it send send signal/data to AWS server and mark attendence.
- In case of unknown person/student it simply says *Unknown*.
- Train before adding students/persons. So that image can be changed to encoding format so that he/she can be recognized 
**Note: Wifi/Internet should be connected to Raspberry Pi to avail this system.**

Preview
---------------
<img src="https://user-images.githubusercontent.com/38128234/57752421-c0394a80-7706-11e9-8af1-ee821544d18c.JPG" wisth="250px" height="250px">
