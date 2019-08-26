import numpy as np
import random
#simulation of families

#input number of families

NumFam = int(input('Number of families: '))

data = np.zeros((3, NumFam))

#print("Data", data, "\n")
#print("Data", np.arange(1, NumFam+1), "\n")

data[0, :] = np.arange(1, NumFam +1)

print("Data", data, "\n\n\n\n")


for x in range(NumFam):
    print("Family ID: ", x+1)
    if random.randint(1,101) > 5:
        while True:
            #girl added to family
            if random.randint(1,101) > 20:
                data[1,x] += 1
                print('Girl ', end='')
            #boy added to family        
            else:
                data[2,x] += 1
                print('Boy')
                break
    else:
        print('No Kids')
    
print("\n\n\nData", data, "\n")