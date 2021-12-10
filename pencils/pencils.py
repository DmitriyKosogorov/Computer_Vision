from skimage import filters
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.measure import regionprops, label
from skimage.filters import threshold_otsu
from skimage.transform import resize
import numpy as np


def longer(region:regionprops):
    bbox=region.bbox
    height=abs(bbox[0]-bbox[2])
    width=abs(bbox[1]-bbox[3])
    if(width<20 or height<20):
        return False
    if(height>width*5 or height*5<width):
        return True
    trues=0
    falses=0
    for i in range(len(region.image)):
        for j in range(len(region.image[1])):
            if(region.image[i,j]==True):
                trues+=1
            else:
                falses+=1
    if(falses>(trues*5)):
        return True
    return False


threshold=0.56
show_regions=False
fin_res=0
for i in range(1,13,1):
    image=plt.imread('img ('+str(i)+').jpg')
    image = resize(image, (1000, 1000),anti_aliasing=True)
    graying=rgb2gray(image)

    graying[graying>threshold_otsu(graying)]=0
    graying[graying!=0]=1      
    labeled=label(graying)

    res=0
    for region in regionprops(labeled):
      if region.perimeter>1400 and longer(region):
        if(show_regions==True):
            plt.imshow(region.image)
            plt.show()
        res+=1
    print('img ('+str(i)+').jpg: ',res)
    fin_res+=res

print('total_number_of_pencils = ',fin_res)
