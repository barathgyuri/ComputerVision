# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

import cv2
import sys



img = cv2.imread(r"femaleFace.jpg")
cv2.imshow("Female Face",img)
cv2.waitKey(0)



cap = cv2.VideoCapture("test_video.mp4")
success = True
while success:
    success, img = cap.read()
    if success:
        cv2.imshow("Video output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



#web Cam

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
success = True
cap.set(10,100)
while success:
    success, img = cap.read()
    if success:
        cv2.imshow("Video output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# %%


