# #!/usr/bin/python
# # coding:utf-8

import cv2
import numpy as np
np.set_printoptions(threshold=1000000)

img = cv2.imread('daibola.jpg', 1)
# # 卷积核
rect = np.array([[0, 0, 0, 0, 0],
                 [0, 0.11, 0.11, 0.11, 0],
                 [0, 0.11, 0.11, 0.11, 0],
                 [0, 0.11, 0.11, 0.11, 0],
                 [0, 0, 0, 0, 0]], np.float32)

bigrect = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                    [0.04, 0.04, 0.04, 0.04, 0.04],
                    [0.04, 0.04, 0.04, 0.04, 0.04],
                    [0.04, 0.04, 0.04, 0.04, 0.04],
                    [0.04, 0.04, 0.04, 0.04, 0.04]], np.float32)

gaussian = np.array([[0.01, 0.02, 0.03, 0.02, 0.01],
                     [0.02, 0.06, 0.08, 0.06, 0.02],
                     [0.03, 0.08, 0.11, 0.08, 0.03],
                     [0.02, 0.06, 0.08, 0.06, 0.02],
                     [0.01, 0.02, 0.03, 0.02, 0.01]], np.float32)

sharpen = np.array([[0, 0, 0, 0, 0],
                    [0.02, 0.06, 0.08, 0.06, 0.02],
                    [0.03, 0.08, 0.11, 0.08, 0.03],
                    [0.02, 0.06, 0.08, 0.06, 0.02],
                    [0.01, 0.02, 0.03, 0.02, 0.01]], np.float32)

edges = np.array([[0, 0, 0, 0, 0],
                  [0, -1, -1, -1, 0],
                  [0, -1,  8, -1, 0],
                  [0, -1, -1, -1, 0],
                  [0, 0, 0, 0, 0]], np.float32)

edges1 = np.array([[0, 0, 0, 0, 0],
                  [0, 0, -2, 0, 0],
                  [0, -2, 8, -2, 0],
                  [0, 0, -2, 0, 0],
                  [0, 0, 0, 0, 0]], np.float32)

shift = np.array([[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]], np.float32)

handshake = np.array([[0.2, 0, 0, 0, 0],
                      [0, 0.2, 0, 0, 0],
                      [0, 0, 0.2, 0, 0],
                      [0, 0, 0, 0.2, 0],
                      [0, 0, 0, 0, 0.2]], np.float32)

nothing = np.array([[0.0001, 0.0001, 0.0001],
                      [0.0001, 0.9992, 0.0001],
                      [0.0001, 0.0001, 0.0001]], np.float32)

nothing = np.array([[1, 1, 1],
                      [1, 8, 1],
                      [1, 1, 1]], np.float32)
# 该函数实际上计算相关性，而不是卷积.  ddepth:目标图像的所需深度
rectimage = cv2.filter2D(img, -1, rect)
bigrectimage = cv2.filter2D(img, -1, bigrect)
gaussianimage = cv2.filter2D(img, -1, gaussian)
sharpenimage = cv2.filter2D(img, -1, sharpen)
edgesimage = cv2.filter2D(img, -1, edges)
edges1image = cv2.filter2D(img, -1, edges1)
shiftimage = cv2.filter2D(img, -1, shift)
handshakeimage = cv2.filter2D(img, -1, handshake)
nothingimage = cv2.filter2D(img, -1, nothing)

print(nothingimage)
print(nothingimage.shape)

# print(img.shape)
# print(gaussianimage.shape)
cv2.imshow('original', img)
cv2.imshow('rect', rectimage)
cv2.imshow('bigrect', bigrectimage)
cv2.imshow('gaussian', gaussianimage)
cv2.imshow('sharpen', sharpenimage)
cv2.imshow('edges', edgesimage)
cv2.imshow('edges1', edges1image)
cv2.imshow('shift', shiftimage)
cv2.imshow('handshake', handshakeimage)
cv2.imshow('nothing', nothingimage)

cv2.imwrite('map/rect.jpg',rectimage)
cv2.imwrite('map/bigrect.jpg',bigrectimage)
cv2.imwrite('map/gaussian.jpg',gaussianimage)
cv2.imwrite('map/sharpen.jpg',sharpenimage)
cv2.imwrite('map/edges.jpg',edgesimage)
cv2.imwrite('map/shift.jpg',shiftimage)
cv2.imwrite('map/handshake.jpg',handshakeimage)

cv2.waitKey(0)
