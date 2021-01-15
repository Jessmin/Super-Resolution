import time

for i in range(100):
    print(f'{i}%', end='\r')
    time.sleep(1)
