# 分析傅里叶级数分解之后cos和sin的和项的图像输出
 
from numpy import mgrid,sin,cos,array,pi
from matplotlib.pyplot import plot,show,title,legend,xlabel,ylabel
 
x = mgrid[0:10:0.02] # 这里类似于MATLAB用冒号产生步长为0.02的序列，但是语法和MATLAB不同
 
 
 
# 下面的这段循环实现y=sin(x)+sin(3x)+...+sin(19x)
 
def cos_square():
  y1 = 0;
  for i in range(0,20,1):
    b = (-1)**(i)*cos((2*i+1)*x)/(2*i+1)
    y1=b+y1    # 这种求和的方法是从C语言移植过来的
  plot(x,y1,'orange',linewidth=0.6)
  title('cos_square')
  xlabel('Time')
  ylabel('Amplitude')
  show()
 
def sin_square():
  y2 = 0
  for i in range(0,20,1):
    b = sin((2*i+1)*x)/(2*i+1)
    y2=b+y2    # 这种求和的方法是从C语言移植过来的
  plot(x,y2,'g',linewidth=0.6)
  title('sin_square')
  xlabel('Time')
  ylabel('Amplitude')
  show()
 
cos_square() 
 
sin_square()
