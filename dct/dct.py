import numpy as np
import cv2
# from matplotlib import pyplot as plt

y = cv2.imread('window.bmp', 0)
# print(y.shape)
cv2.imshow("gray",y)
y1 = y.astype(np.float32)
# print(y1.dtype)
Y = cv2.dct(y1)
print(Y.shape)
for i in range(0,1024):
     for j in range(0,1024):
         if i > 1024 or j > 1024:
             Y[i,j] = 0
cv2.imshow("Dct",Y)
y2 = cv2.idct(Y)
# print(y2.dtype)
cv2.imshow("iDCT",y2.astype(np.uint8))
cv2.waitKey(0)
