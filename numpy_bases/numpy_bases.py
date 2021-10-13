import numpy as np

def is_no_zeros(mas,start,end):
    for i in range(start,end,1):
        if(mas[i]!=0):
            return True
    return False


for i in range(1,7,1):
    filename="figure"+str(i)+".txt"
    file=open(filename)
    print(filename, end=": ")
    size=float(file.readline())
    high=0
    width=0
    file.readline()
    width=len(file.readline().replace("\n","").split(" "))-1
    print(round(width/size,2)," mm/px")
    file.close()


file=open("img1.txt")
file1=open("img2.txt")
for i in range(2):
    file.readline()
    file1.readline()
arr1=np.loadtxt(file)
arr2=np.loadtxt(file1)
sumx1=[]
sumy1=[]
sumx2=[]
sumy2=[]
resultx=-1
resulty=-1
for x in range(arr1.shape[0]):
    sumx1.append(np.sum(arr1[x,:]))
    sumx2.append(np.sum(arr2[x,:]))
for y in range(arr1.shape[1]):
    sumy1.append(np.sum(arr1[:,y]))
    sumy2.append(np.sum(arr2[:,y]))

for i in range(len(sumx1)):
    b=True
    for j in range(len(sumx1)-i):
        if(sumx1[j+i]!=sumx2[j]):
            b=False
            break
    if(b==True):
        if(is_no_zeros(sumx1,i,len(sumx1))):
            resultx=i

for i in range(len(sumy1)):
    b=True
    for j in range(len(sumy1)-i):
        if(sumy1[j+i]!=sumy2[j]):
            b=False
            break
    if(b==True):
        if(is_no_zeros(sumy1,i,len(sumx1))):
            resulty=i


if(resultx==-1):
    for i in range(len(sumx2)):
        b=True
        for j in range(len(sumx2)-i):
            if(sumx2[j+i]!=sumx1[j]):
                b=False
                break
        if(b==True):
            if(is_no_zeros(sumx2,i,len(sumx2))):
                resultx=i

if(resulty==-1):
    for i in range(len(sumy2)):
        b=True
        for j in range(len(sumy2)-i):
            if(sumy2[j+i]!=sumy1[j]):
                b=False
                break
        if(b==True):
            if(is_no_zeros(sumy2,i,len(sumy2))):
                resulty=i
print("difference between images: x=",resultx,", y=",resulty)
