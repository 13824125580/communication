import numpy as np
import pylab as pl
# 50Hz正弦波512点FFT采样t
t= np.arange(0, 1.0, 1.0/8000)
x = np.sin(2*np.pi*50*t)[:512]
pl.plot(np.hstack([x,x,x,x]),linewidth=1)
pl.xlabel('Sampling point')
pl.ylabel('Amplitude[a.u.]')
pl.ylim(-1.5,1.5)
pl.show()
