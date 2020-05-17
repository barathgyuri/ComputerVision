# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import cv2
import sys
import numpy as np


# %%
def getConturs(img):
    conturs,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    ObjectType = ''
    for contur in conturs:
        area = cv2.contourArea(contur)
        print(area)       
        if area>500:
            cv2.drawContours(imgContur,contur,-1,(255,0,0),3)
            peri = cv2.arcLength(contur,True)
            approx = cv2.approxPolyDP(contur,0.02*peri,True)
            print(len(approx))
            objectCorner = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            if objectCorner ==3: ObjectType = "Tri"
            elif objectCorner ==4: 
                aspectRatio = w/float(h)
                if aspectRatio>0.95 and aspectRatio<1.05: ObjectType = "Square"
                else: ObjectType = "Rectangle"
            elif objectCorner>4:ObjectType = "Circle"

            cv2.rectangle(imgContur,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContur,ObjectType,
                (int(x+(w/2)-10),int(y+(h/2)-10)),
                cv2.FONT_HERSHEY_COMPLEX,
                0.8,
                (0,0,0),2)

img = cv2.imread(r"Shapes.png")
imgContur = img.copy()

cv2.imshow("Original",img)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blured Gray Image",imgBlur)

imgCanny = cv2.Canny(imgBlur,50,50)
getConturs(imgCanny)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Contur",imgContur)

cv2.waitKey(0)


# %%


