import numpy as np
import matplotlib.pyplot as plt

image=np.load("ps.npy")


visited=[]

#directions:
#right=1
#down=2
#left=3
#up=4


def get_code(image,x,y,direction):
    global visited
    visited.append([y,x])
    code=''
    if(direction==4):
        if(image[y,x-1]==1 and not([y,x-1] in visited)):
            code=code+get_code(image,x,y,3)
        if(image[y-1,x]==1 and not([y-1,x] in visited)):
            code=code+'4'+get_code(image,x,y-1,4)
        if(image[y,x+1]==1 and not([y,x+1] in visited)):
            code=code+get_code(image,x,y,1)
    elif(direction==1):
        if(image[y-1,x]==1 and not([y-1,x] in visited)):
            code=code+get_code(image,x,y,4)
        if(image[y,x+1]==1 and not([y,x+1] in visited)):
            code=code+'1'+get_code(image,x+1,y,1)
        if(image[y+1,x]==1 and not([y+1,x] in visited)):
            code=code+get_code(image,x,y,2)
    elif(direction==2):
        if(image[y,x+1]==1 and not([y,x+1] in visited)):
            code=code+get_code(image,x,y,1)
        if(image[y+1,x]==1 and not([y+1,x] in visited)):
            code=code+'2'+get_code(image,x,y+1,2)
        if(image[y,x-1]==1 and not([y,x-1] in visited)):
            code=code+get_code(image,x,y,3)
    elif(direction==3):
        if(image[y+1,x]==1 and not([y+1,x] in visited)):
            code=code+get_code(image,x,y,2)
        if(image[y,x-1]==1 and not([y,x-1] in visited)):
            code=code+'3'+get_code(image,x-1,y,3)
        if(image[y-1,x]==1 and not([y-1,x] in visited)):
            code=code+get_code(image,x,y,4)
    
    return(code)    


def make_mask(code):
    mask=np.array([[1,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0]])
    x=0
    y=0
    for i in code:
        if(i=='1'):
            x=x+1
        if(i=='2'):
            y=y+1
        if(i=='3'):
            x=x-1
        if(i=='4'):
            y=y-1
        mask[y,x]=1
    return(mask)

dict={}
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        if(image[y,x]==1 and not([y,x] in visited)):
            coder=get_code(image,x,y,1)

            if(coder in dict.keys()):
                dict[coder]+=1
            else:
                dict[coder]=1

dict1={}
masks=[]
for key in dict.keys():
    str=''.join(sorted(key))
    if(str in dict1.keys()):
        dict1[str]+=dict[key]
    else:
        dict1[str]=dict[key]
        masks.append(make_mask(key))


b=0
for key in dict1.keys():
    print(dict1[key],': ')
    print(masks[b])
    print()
    b+=1

    
plt.imshow(image)
plt.show()
