# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import cv2
import sys
import numpy as np


# %%
img = cv2.imread(r"FruitBasket.jpg")
kernel = np.ones((5,5),np.uint8)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Fruti Basket Gray",imgGray)
cv2.imshow("Fruti Basket Gray Blur",imgBlur)
cv2.imshow("Fruti Basket Canny",imgCanny)
cv2.imshow("Fruti Basket Dialation",imgDialation)
cv2.imshow("Fruti Basket Erosion",imgEroded)
cv2.waitKey(0)


# %%


