#coding:utf-8
import numpy as np
from scipy import fftpack,signal
import matplotlib.pyplot as plt
b = 30
f_s = 800
N = 8000
t = np.linspace(0, 10, N, endpoint=False)
sq = signal.square(2 * np.pi * 5 * t)

F = fftpack.fft(sq)
f = fftpack.fftfreq(N, 1.0/f_s)
mm=(abs(f) < 5)
# F_filtered = F * (abs(f) < 5)
F_filtered = F 
print(F_filtered)
print(f)
print(f.shape)
ift = fftpack.ifft(F_filtered)
mask = np.where(f >= 0)

print(f[mask].shape)
print(mask)
print(f[mask])
print(mm)
fig, axes = plt.subplots(5,1)
axes[0].plot(t, sq)
axes[0].set_ylim(-2, 2)
axes[1].plot(f[mask], abs(F[mask]/N), label="freq")
axes[2].plot(t,ift.real, label="all")
axes[3].plot(t,ift.real, label="zoom")
axes[3].set_xlim(1, 2)
M=abs(F)
print(M[501])
intval = np.linspace(0, N, N, endpoint=False)
print(np.argmax(M))
axes[4].plot(intval,M, label="zoom")
plt.show()
