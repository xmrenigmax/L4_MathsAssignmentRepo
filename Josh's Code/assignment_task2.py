import numpy as np
from assignment_task1 import mean_of_z

a = 13
u = (1 + 1j)
z_num = np.sqrt(2)*u
z_den = np.power((u/np.sqrt(2)), a)
z_intial =  z_num / z_den
b = 5 + 6

z_list = np.array([z_intial])
step = (np.sqrt(2))/(1 + 1j)

count = 0
found = False
while not found:
    

    z_pos = z_list[count]
    z_pos_nPlus1 = z_pos/step
    
    z_list = np.append(z_list, z_pos_nPlus1 )
    new_mean = np.mean(z_list)

    if np.isclose(new_mean, 0, atol= 1e-3):
        found = True
        print(f'Found at step {count}')
        
    else:
        count += 1
    
    if count == 1000:
        print('nope')
        break