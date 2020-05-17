# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import cv2
import sys
import numpy as np


# %%
img = cv2.imread(r"eye.jpg")
print(img.shape)



imgResize = cv2.resize(img, (300,200))
imgCropped = img[:200,200:500]
cv2.imshow("Eye",img)
cv2.imshow("Eye Resized",imgResize)
cv2.imshow("Eye Cropped",imgCropped)
cv2.waitKey(0)


# %%


