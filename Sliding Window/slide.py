import cv2
import numpy as np
import os
cwd = os.getcwd()

HRP=cv2.imread('GILGIT.jpg')

a = 25.222266 
b = 62.172388
c = 0.000686646/2
d = 0.000585503/2
i=1
j=1
count = 1

print(HRP)
# print(cwd + '/results/' + str(b) + '_' + str(a) + '.jpg')
while(j+255 <= np.size(HRP,0)):
    i = 1
    b = 62.172388
    while (i+255 <= np.size(HRP,1)):
        if ((count/(5476*4) * 100) > 60):
            
            first = j+255
            second = i+255
            path = cwd + '/results/' + str(b) + '_' + str(a) + '.jpg'
            cv2.imwrite(path, HRP[int(j):int(first),int(i):int(second)])
    
        b = b + c
        i = i + 256/2
        count = count + 1
    
    count/(5476*4) * 100
    a = a -d
    j = j + 256/2