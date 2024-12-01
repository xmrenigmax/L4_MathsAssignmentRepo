import math
import numpy as np

def task2():
    a = 13
    count = 0

    zinitial = (math.sqrt(2) * (1 + 1j)) / (((1 + 1j) / math.sqrt(2))**a)

    z_list = np.array([zinitial])
    u = math.sqrt(2) / (1 + 1j)

    while count < 64:
        zposition = z_list[count] / u
        z_list = np.append(z_list, zposition)
        zpositionmean2 = np.mean(z_list)

        if np.isclose(zpositionmean2, 0, atol=1e-1):
            print(f"Count: {count}")
            break
        count += 1

task2()

