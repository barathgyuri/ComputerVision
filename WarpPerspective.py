# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import cv2
import sys
import numpy as np


# %%
img = cv2.imread(r"cards2.jpg")
width, height = 250,350
pts1 = np.float32([[590,240],[778,305],[432,420],[651,506]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Wrapped",imgOutput)
cv2.imshow("Original",img)
cv2.waitKey(0)


# %%


