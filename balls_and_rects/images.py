import matplotlib.pyplot as plt
import numpy as np
from skimage import color
from skimage.measure import label, regionprops

def det_color(hsv):
    info=np.unique(image[:,:,0])
    sumdif=0
    for i in range(1,len(info)):
        sumdif+=(info[i]-info[i-1])
    dif=sumdif/(len(info))
    k=0
    res=[[info[0],-1]]
    for i in range(1,len(info),1):
        if(abs(info[i]-info[i-1])>dif):
            res[k][1]=info[i-1]
            res.append([info[i],-1])
            k+=1
    res[k][1]=info[len(info)-1]
    res1=[]
    for i in range(len(res)):
        if((res[i][1]+res[i][0])/2!=0):
            res1.append((res[i][1]+res[i][0])/2)
    return res1

def all_equals(image,coords):
    color=image[coords[0],coords[1]]
    for i in range(coords[0]+1,coords[2]-1,1):
        for j in range(coords[1]+1,coords[3]-1,1):
            if(image[i,j]!=color):
                return(False)
    return(True)


image=plt.imread('balls_and_rects.png')
binary=np.sum(image,2)
binary[binary>0]=1

image=color.rgb2hsv(image)

colors=det_color(image)
rounds={}
rects={}
defolt_color=colors[0]
for colorec in colors:
    rounds[colorec]=0
    rects[colorec]=0
   
labeled=label(binary)
regions=regionprops(labeled)
i=0
for region in regions:
    current_color=image[int((region.bbox[0]+region.bbox[2])/2),int((region.bbox[1]+region.bbox[3])/2),0]
    diff=100000
    target_color=defolt_color
    for colorec in colors:
        if(abs(current_color-colorec)<diff):
            diff=abs(current_color-colorec)
            target_color=colorec       
    if(not all_equals(labeled, region.bbox)):
        rounds[target_color]+=1
    else:
        rects[target_color]+=1
    i+=1
summ=0

for key in rounds.keys():
    summ+=rounds[key]
print('Total number of rounds ',summ)
summ_all=summ
indexx=1
for key in rounds.keys():
    print(indexx,': ',rounds[key])
    indexx+=1
print()
indexx=1
summ=0
for key in rects.keys():
    summ+=rects[key]
print('Total number of rectangles ',summ)    
for key in rects.keys():
    print(indexx,': ',rects[key])
    indexx+=1
summ_all+=summ

print('total number of figures: ',summ_all)

diagram=[]
for i in range(100):
    diagram.append([])
    for colorec in colors:
        for j in range(100):
            diagram[i].append([colorec,1,1])
diagram=np.array(diagram)
diagram=color.hsv2rgb(diagram)
plt.title(f'Colors from 1 to {len(colors)}')
plt.imshow(diagram)
