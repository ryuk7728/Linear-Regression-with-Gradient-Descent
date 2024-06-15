import matplotlib.pyplot as plt
import numpy as np

def computeDerivativeW(x,y,w,b,m):
    derW=0
    for i in range(m):
        derW+=(w*x[i]+b-y[i])*x[i]
    derW/=m
    return derW

def computeDerivativeB(x,y,w,b,m):
    derB=0
    for i in range(m):
        derB+=(w*x[i]+b-y[i])
    derB/=m
    return derB

 




x=np.array([1.  ,  2.  ,  3.  ,  4.  ,  5.  ,  6.  ,  7.  ,  8.  ,  9.  , 10.  ,
     11.  , 12.  , 13.  , 14.  , 15.  , 16.  , 17.  , 18.  , 19.  , 20.  ,
     21.  , 22.  , 23.  , 24.  , 25.  , 26.  , 27.  , 28.  , 29.  , 30.  ,
     31.  , 32.  , 33.  , 34.  , 35.  , 36.  , 37.  , 38.  , 39.  , 40.  ,
     41.  , 42.  , 43.  , 44.  , 45.  , 46.  , 47.  , 48.  , 49.  , 50.])
y=np.array([53.46418758,  28.51537397,  90.22254236, 151.37827831, 162.73237625,
      48.72827626, 181.53950925, 137.09126865, 122.36947494, 160.19328773,
     111.25926829, 155.42453027, 163.08420671, 133.64491597, 219.12666904,
     178.11729841, 197.87393852, 144.7547868 , 161.54010428, 157.01778563,
     259.22400534, 216.41198288, 224.74245016, 185.61581034, 261.17370598,
     258.10681832, 234.00993946, 246.12404075, 253.58836882, 224.24360335,
     280.85412115, 232.6205363 , 225.54482654, 314.77494935, 314.77862651,
     344.22704126, 319.9490023 , 285.20799891, 352.92965219, 324.61617777,
     317.90507036, 301.48450784, 320.64372898, 347.46097345, 388.10814686,
     336.35010727, 375.75701883, 397.45409947, 389.94022145, 409.33059717])
m=len(x)
w=0
b=0
iter=100000
alpha=0.001
lossx=[]
loss=[]


plt.scatter(x, y, color='blue', label='Data points')

for i in range(iter):
    lossx.append(i)
    tempW=w-alpha*computeDerivativeW(x,y,w,b,m)
    tempB=b-alpha*computeDerivativeB(x,y,w,b,m)
    w=tempW
    b=tempB
    loss.append(sum((w*x+b-y)**2)/50)



xp = np.linspace(0, 50, 500)
yp = w * xp + b

plt.plot(xp, yp, color='red', label=f'y = {w:.2f}x + {b:.2f}')
plt.title("Linear Regression")
plt.legend()
plt.show()

plt.plot(lossx, loss, color='blue', label='Data points')
plt.title("Loss Curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.show()

