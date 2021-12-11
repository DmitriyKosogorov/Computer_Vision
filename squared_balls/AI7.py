import cv2
import numpy as np
from random import shuffle

camera=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cv2.namedWindow('Camera',cv2.WINDOW_KEEPRATIO)
cv2.namedWindow('Background',cv2.WINDOW_KEEPRATIO)
position=[]


def on_mouse_click(event,x,y,flags, param):
    if(event==cv2.EVENT_LBUTTONDOWN):
        global position
        print(position)
        position=[y,x]

cv2.setMouseCallback('Camera',on_mouse_click)


measures=[]
lower1=(150,190,180)
lower2=(0,153,185)
lower3=(55,150,150)
red=((110,120,160),(180,255,255))
yellow=((10,120,180),(50,255,255))
blue=((65,150,150),(105,255,255))
green=((44,100,150),(85,255,255))
d=5.6
radius=1

hsv_color=[]

random_orderich=['red','blue','yellow','green']
shuffle(random_orderich)
random_orderich=[[random_orderich[0],random_orderich[1]],
                 [random_orderich[2],random_orderich[3]]]
print(random_orderich)
answer=None
while camera.isOpened():
    _,image=camera.read()
    blurred=cv2.GaussianBlur(image,(11,11),0)
    hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
    maskr=cv2.inRange(hsv,red[0],red[1])
    masky=cv2.inRange(hsv,yellow[0],yellow[1])
    maskb=cv2.inRange(hsv,blue[0],blue[1])
    maskg=cv2.inRange(hsv,green[0],green[1])
    masks={'red':maskr,'blue':maskb,'yellow':masky,'green':maskg}
    coords={}
    for key in masks.keys():
        mask=masks[key]
        mask=cv2.erode(mask,None,iterations=2)
        mask=cv2.dilate(mask,None,iterations=2)
        cnts=cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
        if(len(cnts)>0):
            c=max(cnts,key=cv2.contourArea)
            (curr_x,curr_y),radius=cv2.minEnclosingCircle(c)
            coords[key]=[curr_x,curr_y]
            if(radius>10):
                cv2.circle(image,(int(curr_x),int(curr_y)),int(radius),(0,255,255),2)
                cv2.circle(image,(int(curr_x),int(curr_y)),5,(0,255,255),2)
    #coords={'red':[1,1],'blue':[1,2],'yellow':[2,1],'green':[2,2]}
    if(len(coords.keys())==4):
        correct_order_row=True
        correct_order_column=True
        for row in random_orderich:
            old_coord=0
            for color in row:
                if(color in coords.keys() and coords[color][1]>=old_coord):
                    old_coord=coords[color][1]
                else:
                    correct_order_row=False
        
        for i in range(2):
            if(random_orderich[0][i] in coords.keys() and random_orderich[1][i] in coords.keys() and coords[random_orderich[0][i]][0]<=coords[random_orderich[1][i]][0]):
                print('',end='')
            else:
                correct_order_column=False
        
        if(correct_order_row==True and correct_order_column==True and (answer ==None or answer==False)):
            print('Correct!')
            answer=True
        if(correct_order_row==False and correct_order_column==False and (answer==None or answer == True)):
            print('Incorrect')
            answer=False

    key=cv2.waitKey(1)
    if(key==ord('q')):
        break
    cv2.imshow('Camera', image)
camera.release()
cv2.destroyAllWindows()