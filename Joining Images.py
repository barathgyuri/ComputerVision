# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import cv2
import sys
import numpy as np


# %%
img = cv2.imread(r"puppy.jpg")
img = cv2.resize(img,(300,450))
print(img.shape)
cv2.imshow("Original",img)
imgHorizontal = np.hstack((img,img))
cv2.imshow("Stacked Horizontal",imgHorizontal)
imgVertial = np.vstack((img,img))
cv2.imshow("Stacked Vertical",imgVertial)
cv2.waitKey(0)


# %%


