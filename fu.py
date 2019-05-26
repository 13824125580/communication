import numpy as np
import pylab as pl
import math

# b=[1,0,-1,0]
b=[0,0,0,0,0,0,0,0]
y=np.fft.fft(b) *2/8
absY=[np.abs(x) for x in y]
print(y)
print(absY[0])
print(absY[1])
print(absY[2])
print(absY[3])
print(absY[4])
print(absY[5])
print(absY[6])
print(absY[7])
print(math.atan2(y[0].imag,y[0].real)*180/math.pi)
print(math.atan2(y[1].imag,y[1].real)*180/math.pi)
print(math.atan2(y[2].imag,y[2].real)*180/math.pi)
print(math.atan2(y[3].imag,y[3].real)*180/math.pi)
print(math.atan2(y[4].imag,y[4].real)*180/math.pi)

