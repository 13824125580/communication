# -*- coding: -utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

N = 256
x = np.linspace(-10, 10, N)
y = np.linspace(-10, 10, N)

print(x)
print(y)
Y,X = np.meshgrid(x,y)

print(X)
print(Y)
Z = 30 * np.cos(200 * np.pi * X)     #光栅

Z_fft2 = np.fft.fft2(Z)

Z_fft2_sh = abs(np.fft.fftshift(Z_fft2))

plt.subplot(441)
plt.imshow(Z)
plt.title('Original')


plt.subplot(442)
plt.imshow(abs(Z_fft2))
plt.title('fft2')


plt.subplot(443)
plt.imshow(Z_fft2_sh)
plt.title('fft2-shift')

plt.subplot(444)
plt.plot(X)
plt.title('X')

plt.subplot(445)
plt.plot(Y)
plt.title('Y')

plt.subplot(446)
plt.plot(Z_fft2_sh[128,:])
plt.title('x = 128')

plt.subplot(447)
plt.plot(Z_fft2_sh[:,128])
plt.title('y = 128')

plt.subplot(448)
plt.plot(Z_fft2_sh[:,127])
plt.title('y = 127')

plt.subplot(449)
plt.plot(Z_fft2_sh[1,:])
plt.title('x = 1')

plt.subplot(4,4,10)
plt.plot(Z_fft2_sh[64,:])
plt.title('x = 64')

plt.subplot(4,4,11)
plt.plot(Z_fft2_sh[120,:])
plt.title('x = 120')

plt.subplot(4,4,12)
plt.plot(Z_fft2_sh[127,:])
plt.title('x = 127')

plt.subplot(4,4,13)
plt.plot(Z_fft2_sh[255,:])
plt.title('x = 255')

plt.subplot(4,4,14)
plt.plot(Z_fft2_sh[192,:])
plt.title('x = 192')

plt.subplot(4,4,15)
plt.plot(Z_fft2_sh[136,:])
plt.title('x = 136')

plt.subplot(4,4,16)
plt.plot(Z_fft2_sh[129,:])
plt.title('x = 129')

plt.show()
