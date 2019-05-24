import numpy as np
import pylab as pl
import math
# 采样步长
w=1048
t = [x/w for x in range(w)]
# 设计的采样值
y = [2.0 + 3.0 * math.cos(2.0 * math.pi * 50 * t0 - math.pi * 30/180)
    + 1.5 * math.cos(2.0 * math.pi * 75 * t0 + math.pi * 90/180)
    +  1.0 * math.cos(2.0 * math.pi * 150 * t0 + math.pi * 120/180)
    +  2.0 * math.cos(2.0 * math.pi * 220 * t0 + math.pi * 30/180)
    for t0 in t ]

N=len(t)
fs=w
df=fs/(N-1)
f=[df*n for n in range(0,N)]

Y=np.fft.fft(y)*2/N
absY=[np.abs(x) for x in Y]
# print(t.shape)
# print(N.shape)
print(len(y))
print(len(Y))
print(N)
# print(y)
# m = 0
# i = 0
# while i < len(y):
    # m = m +y[i]
    # i+=1
# print(m)

# print(N)
# print(df)

i=0
while i < len(absY):
	if absY[i]>0.01:
                print('freq:%d : %5.2f + %5.2f j, A:%3.2f, phi: %6.1f' % (i, Y[i].real, Y[i].imag, absY[i],math.atan2(Y[i].imag,Y[i].real)*180/math.pi))
	i+=1
timezone=pl.subplot(211)
timezone.plot(t,y)
freqzone=pl.subplot(212)
freqzone.plot(f,absY)
pl.show()
