import cv2
import numpy as np
import winsound
import time

kernelBlur = 11
kernelDilate = 1
conf = 15
kernelDilate = np.ones((5,5) , np.uint8)
surface = 1000
confMotion = 5000
videoDir = "e:\\Record\\"
videoExtension = 100

MUTE = "mute"
DETECT = "detect"

cap = cv2.VideoCapture(0)
_ , original = cap.read()
original = cv2.resize(original , (720,500))
original = cv2.cvtColor(original , cv2.COLOR_BGR2GRAY)
original = cv2.GaussianBlur(original , (kernelBlur , kernelBlur) , 0)

alarm = False
mode = DETECT
videoFile = None
cptMotion = 0

while True:
    ret , frame = cap.read()
    frame = cv2.resize(frame , (720,500))
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray , (kernelBlur , kernelBlur) , 0)
    
    mask = cv2.absdiff(original , gray)
    mask = cv2.threshold(mask , conf , 255 , cv2.THRESH_BINARY)[1]
    
    
    #Mode local avec utilisation d'une seuil de surface
    if mode == MUTE:
        alarm = False
        sum = "Mute mode"
        mask = cv2.dilate(mask , kernelDilate , iterations=2)
        contours , nada = cv2.findContours(mask , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
        frame_contour = frame.copy()
        for c in contours:
            x , y , w , h = cv2.boundingRect(c)
            if cv2.contourArea(c) < surface:
                continue
            cv2.rectangle(frame_contour , (x,y) , (x+w , y+h) , (0,0,255) , 2)
            
    #Mode globale
    else:
        sum = int(np.sum(mask)/255)
        contours , _ = cv2.findContours(mask , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
        frame_contour = frame.copy()
        for c in contours:
            cv2.drawContours(frame_contour , [c] , 0 , (0,255,0) , 5)
        if sum > confMotion:
            alarm = True
        else:
            alarm = False
            
            
    if alarm:
        print('ALARM!!!' , end='\t')
        winsound.Beep(3000 , 10)
        cv2.circle(frame_contour , (360,250) , 10 , (0,0,255) , -1)
        if videoFile is None:
            videoFile = time.strftime("%Y.%m.%d.%H.%M.%S")+".avi"
            video = cv2.VideoWriter(videoFile , cv2.VideoWriter_fourcc(*'DIVX'), 15 , (720,500))
        video.write(frame)
        cptMotion = videoExtension
    else:
        if cptMotion is not 0:   
            cptMotion = cptMotion - 1
        if videoFile is not None:
            if cptMotion == 0:
                video.release()
                videoFile = None
            else:
                video.write(frame)
                cv2.circle(frame_contour , (360,250) , 10 , (0,0,255) , -1)
    
    cv2.rectangle(frame_contour , (0,0) , (frame.shape[0]*2 , 25) , (255,255,255) , -1)
    cv2.putText(frame_contour , f'Blur:{kernelBlur}(p|m)    Surface de confidence: {surface}(o|l)   Mode: {mode}(s)    Pixel:{sum}' , (5 ,20) , cv2.FONT_HERSHEY_PLAIN , 1 , (0,0,0) , 1)
    #cv2.imshow("Contour" , frame)
    
    cv2.imshow("frame" , frame_contour)
    cv2.resizeWindow('frame' , 720 , 500)
    #cv2.imshow("Main" , mask)
    
    
    original = gray
    key = cv2.waitKey(1)&0xFF
    
    if key == ord('q'):
        break
    
    if key == ord('s'):
        
        if mode == DETECT:
            mode = MUTE
        else:
            mode = DETECT 
    
    if key == ord('p'):
        kernelBlur = kernelBlur + 2
        
    if key == ord('m'):
        kernelBlur = kernelBlur - 2 if kernelBlur > 3 else 1

    if key == ord('o'):
        surface = surface + 50
        
    if key == ord('l'):
        surface = surface - 50 if surface > 50 else 50

cap.release()
cv2.destroyAllWindows()
        