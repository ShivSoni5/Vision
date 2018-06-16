#!/usr/bin/python3

import cv2

def abuse(word):
    cap = cv2.VideoCapture(0)
    status,frame = cap.read()
    cv2.imwrite(f'/home/raj/Pictures/Vision/{word}.png',frame)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    cap.release()

