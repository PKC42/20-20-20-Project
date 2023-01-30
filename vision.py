import cv2
import numpy as np
import time
from datetime import date
from datetime import datetime


def seek_and_detect():

    current_time = datetime.now()

    file = open("log.txt", "w")
    file.write("Session Start Date and Time: {}".format(current_time))

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    camera = cv2.VideoCapture(0)

    if camera.isOpened() == False:
        return False


    while True:
        ret, frame = camera.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        eyes_copy =  eye_cascade.detectMultiScale(gray)
        
        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
        
            eyes = eye_cascade.detectMultiScale(roi_gray)
            eyes_copy = eyes
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            

        if len(faces) > 0 or len(eyes_copy) > 0:
            print("At Computer")
        else:
            print("Away From Computer")
    
        
        cv2.imshow('Video', frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

        

    camera.release()
    cv2.destroyAllWindows()
    file.close()

    return True