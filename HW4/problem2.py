import numpy as np
import matplotlib.pyplot as plt

R,w=1,1

t=np.linspace(0,4*np.pi,50)

x=[]
y=[]

for i in t:
    x.append(np.cos(i))
    y.append(np.sin(i)*2)
plt.plot(x,y)
plt.xlabel('t')
plt.ylabel('Amplitude')
plt.savefig('2.png',dpi=600)
plt.show()