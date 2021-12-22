import time
import pyautogui
import cv2
import mss
import numpy

def all_equal(mas):
    basic=mas[0,0]
    for i in range(mas.shape[0]):
        for j in range(mas.shape[1]):
            if(int(mas[i,j])-int(basic)>100 or int(mas[i,j])-int(basic)<-100):
                #print(mas[i,j],' ', mas[0,0],' ',basic)
                #print(int(mas[i,j])-int(basic))
                return(False) 
    return(True)

def get_trouble(mas):
    total=0
    for i in range(mas.shape[0]):
        if(mas[i,mas.shape[1]-1]<200):
            total+=1
    if(total==0):
        return('medium')
    total=0
    for i in range(mas.shape[0]):
        if(mas[i,0]<200):
            total+=1
    if(total==0):
        return('flying')
    else:
        return('high')
    

pyautogui.PAUSE=0

screenWidth, screenHeight = pyautogui.size()
top=int(screenHeight/4)
left=int(screenWidth/3)
width=int(screenHeight/2)
height=int(screenWidth/14)
barrier_flying=[screenWidth/22,screenHeight/20,screenWidth/15,screenHeight/15]
underdino=[int(screenWidth/90),int(screenHeight/10),int(screenWidth/30),int(screenHeight/9)]
top_line=96
down_line=160
first_line=90
first_check_line=int(screenWidth/20)
#second_line=140
second_line=200
second_check_line=int(screenWidth/18)
jump=False
start_time=time.time()
time_jump=time.time()
time_down=0
timedif1=0.000001
timedif_down=0.4
timedif2=30
prisel=False
upped_times=0
with mss.mss() as sct:
    monitor = {"top": top, "left": left, "width": width, "height": height}
    while True:
        img = numpy.array(sct.grab(monitor))
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        cv2.imshow('Image',img[(down_line-72):(down_line-70), first_line:(second_line-20)])

        if(not all_equal(img[(down_line-72):(down_line-70), (first_line):(second_line-20)])):
            pyautogui.keyDown('down')
            time_down=time.time()
            prisel=True
        
        if(not all_equal(img[(down_line-2):down_line,first_line:second_line])):
                #print(get_trouble(img[top_line+12:down_line,first_check_line:second_check_line]))
                pyautogui.keyDown('up')
                time_jump=time.time()
                jump=True

                
        if(time.time()-time_jump>timedif1 and jump==True):
            jump=False
            pyautogui.keyUp('up')

        if(time.time()-time_down>timedif_down and prisel==True):
            prisel=False
            pyautogui.keyUp('down')

        if(time.time()-start_time>timedif2 and upped_times<=10):
            second_line+=25
            upped_times+=1
            print('upped')
            timedif2=10
            start_time=time.time()
        
        key=cv2.waitKey(1)
        if(key==ord('q')):
            break
