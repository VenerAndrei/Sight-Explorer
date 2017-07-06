import cv2
import serial

#Importing the CASCADE CLASSIFIER for detecting the face.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Accessing the web camera
cap = cv2.VideoCapture(0)

#Connecting to Arduino
port = serial.Serial("COM3",9600)

#Main loop
while(1):

    #Frame Capture
    _, frame = cap.read()

    #Converting to Gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detecting faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        if x<=160:
            port.write(1)           #LEFT
        elif x > 160 and x < 480:
            port.write(2)           #STAY
        elif x >= 480:
            port.write(3)           #RIGHT
        else:
            port.write(2)           #STAY
