import os
import time

clear = lambda: os.system('cls')
spin=['|','/','-','\\','|','/','-','\\']

clear()

for i in range (0,1000):
    print('  '+spin[i%8])
    time.sleep(0.5)
    clear()
