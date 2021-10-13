
import numpy as np
import matplotlib.pyplot as plt

size = 100
image = np.zeros((size, size, 3), dtype="uint8")

size1=size*2
color1 = [255, 128, 0]
color2 = [0, 128, 255]
diff=[(color1[0]-color2[0])/size1,(color1[1]-color2[1])/size1,(color1[2]-color2[2])/size1]
k=0

for i in range(size):
    r=(color1[0]-diff[0]*k)
    g=(color1[1]-diff[1]*k)
    b=(color1[2]-diff[2]*k)
    k=k+1
    for j in range(i+1):
        image[j,i-j,:]=[r,g,b]


print()
for i in range(size-1,0,-1):
    r=(color1[0]-diff[0]*k)
    g=(color1[1]-diff[1]*k)
    b=(color1[2]-diff[2]*k)
    k=k+1
    for j in range(i):
        image[size-i+j,size-j-1,:]=[r,g,b]


plt.figure(1)
plt.imshow(image)
plt.show()