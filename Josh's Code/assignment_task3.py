import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math
a = 13
mpl.rcParams['font.size']=14

x = np.linspace(-10, 5, 1000)

y_num = (x-3)*(1/np.exp(x-3))
y_den = x*np.exp(-a*x)


y = y_num/y_den

plt.plot(x, y, 'g--')
plt.plot(x, y_num, 'r--')
plt.plot(x, y_den, 'b--')

plt.axhline(0, c='black', linewidth=1)
plt.axvline(0, c='black', linewidth=1)


plt.legend([r'$\frac{(x-3).1/e^{x-3}}{x.e^{-a.x}}$'])
plt.xlabel('x')
plt.ylabel('y', rotation=0)
plt.ylim(-10, 10)  
plt.xlim(-10, 5)   


plt.grid()
plt.show()

