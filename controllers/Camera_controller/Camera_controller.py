from controller import Camera
from controller import Robot
import numpy as np
import cv2

from multiprocessing.connection import Client

conn = Client(('localhost', 6000))
conn2 = Client(('localhost', 6001))

robot=Robot()
timestep = int(robot.getBasicTimeStep())
camera = Camera("camera")
camera.enable(timestep)

cv2.startWindowThread()
cv2.namedWindow("preview")

lower_red = np.array([0, 43, 46])
upper_red = np.array([10,255,255])

object_x = 0
object_y = 0
flag = 0
while robot.step(timestep) != -1:
    cameraData = camera.getImage();
    image = np.frombuffer(cameraData, np.uint8).reshape((camera.getHeight(),camera.getWidth(), 4))

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red)

    sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpen = cv2.filter2D(mask, -1, sharpen_kernel)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    close = cv2.morphologyEx(sharpen, cv2.MORPH_CLOSE, kernel, iterations=2)

    cnts=cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    min_area = 500
    max_area = 30000
    for c in cnts:
        area = cv2.contourArea(c)
        if area > min_area and area < max_area:
            x,y,w,h = cv2.boundingRect(c)
            cv2.putText(image, "center: ({}, {})".format(x+w/2, y+h/2), (x, y-40), cv2.FONT_HERSHEY_COMPLEX, 0.5, (36, 255, 12), 1)
            cv2.rectangle(image, (x, y), (x+w, y+h), (3,218,218), 2)
            if(x > 300 and flag == 0):
                flag = 1
            if(flag == 2 and x != object_x and y != object_y):
                flag = 0
            if flag == 1:
                conn2.send('stop')
                conn.send('{}, {}'.format(x+w/2, y+h/2))
                print("current position:"+str(x+w/2)+" "+str(y+h/2))
                flag = 2
            object_x = x
            object_y = y 
        if area < min_area:
            conn2.send('start')
    cv2.imshow("preview", image)
    cv2.waitKey(5 * timestep)

conn.close()
conn2.close()
