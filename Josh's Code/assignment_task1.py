import math
import numpy as np
import matplotlib.pyplot as plt


a = 13
u = 1 + 1j
z_num = (1 + 1j)
z_den = np.sqrt(2)*np.power(1j,4)*np.power((u/np.abs(u)), a)
z_inital = z_num/z_den

#print(z_num)
#print(z_den)
#print(z_inital)
#plt.plot(z_num.real, z_num.imag, 'bx')
#plt.plot(z_den.real, z_den.imag, 'ro')
#plt.plot(z_inital.real, z_inital.imag, 'kx')


z_list = np.array([z_inital])
step = (np.sqrt(2))/(1 + 1j)

for i in range(64):

    z_pos_n = z_list[i]
    z_pos_nPlus_1 =  z_pos_n / step
    z_list = np.append(z_list, z_pos_nPlus_1 )



for j in z_list:
    plt.plot(j.real, j.imag, 'bo')


plt.axhline(0, c='black', linewidth=1)
plt.axvline(0, c='black', linewidth=1)
plt.xlabel('y')
plt.ylabel('x', rotation=0)
#plt.ylim(-0.025, 0.025)  
#plt.xlim(-0.025, 0.025)   


mean_of_z = np.mean(z_list)
print(mean_of_z)
#print(mean_of_z)
plt.quiver(0,0, mean_of_z.real, mean_of_z.imag)
#for i in z_list:
    #print(i)

#plt.show()