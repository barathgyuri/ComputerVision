# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import cv2
import numpy as np


# %%
myColors = [[0,199,17,7,255,255],
            [108,178,13,124,255,119],
            [39,129,51,103,255,255]]


def findColor(img):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        cv2.imshow(str(color[0]),mask)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
success = True
cap.set(10,100)
while success:
    success, img = cap.read()
    findColor(img)
    if success:
        cv2.imshow("Video output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# %%


