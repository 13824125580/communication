import cv2
import numpy as np
import matplotlib.pyplot as plt

# np.set_printoptions(threshold=1000000000)
img = cv2.imread('window.bmp', 0)
img1 = img.astype('float')
print(img1-img)
C_temp = np.zeros([8, 8])
dst = np.zeros([8, 8])
 
m = 8
n = 8
N = n
C_temp[0,:] = 1 * np.sqrt(1/N)
 
for i in range(1, m):
     for j in range(n):
          C_temp[i, j] = np.cos(np.pi * i * (2*j+1) / (2 * N )
) * np.sqrt(2 / N )

C_zhuanzhi = np.transpose(C_temp);
print(C_temp) 
dst = np.dot(C_temp , C_zhuanzhi)
print(dst) 
print(N)
print(C_temp[0, :]) 
print(C_zhuanzhi[:0]) 
