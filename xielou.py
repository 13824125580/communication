# -*- coding:utf-8 -*-
import numpy as np
from math import pi
import matplotlib.pyplot as plt
import matplotlib
import scipy.signal as signal
import math
t = np.arange(0, 1.0, 1.0/8000)
x = np.sin(2*np.pi*50*t)[:512]
# x = [1,2,3,4,5,6,7,8]
plt.plot(np.hstack([x,x,x,x,x]))
plt.show()
