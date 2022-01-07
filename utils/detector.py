import time
import winsound
from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtGui import QImage
import cv2
import numpy as np

class CamWorker(QThread):
    ImageUpdate = pyqtSignal(QImage)
    
    def run(self):
        start = None
        end = None
        self.sum = 0
        self.kernelBlur = 11
        kernelDilate = 1
        conf = 15
        kernelDilate = np.ones((5,5) , np.uint8)
        surface = 1000
        self.confMotion = 5000
        videoDir = "e:\\Record\\"
        videoExtension = 100

        MUTE = "mute"
        DETECT = "detect"

        cap = cv2.VideoCapture(0)
        _ , original = cap.read()
        original = cv2.resize(original , (720,500))
        original = cv2.cvtColor(original , cv2.COLOR_BGR2GRAY)
        original = cv2.GaussianBlur(original , (self.kernelBlur , self.kernelBlur) , 0)

        alarm = False
        mode = MUTE
        videoFile = None
        cptMotion = 0
        
        self.threadActive = True
        
        while self.threadActive:
            
            start = time.time()
            ret , frame = cap.read()
            frame = cv2.resize(frame , (720,500))
            gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray , (self.kernelBlur , self.kernelBlur) , 0)
            
            mask = cv2.absdiff(original , gray)
            mask = cv2.threshold(mask , conf , 255 , cv2.THRESH_BINARY)[1]
            
            
            #Mode local avec utilisation d'une seuil de surface
            if mode == MUTE:
                alarm = False
                sum = 0
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
                self.sum = int(np.sum(mask)/255)
                contours , _ = cv2.findContours(mask , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
                frame_contour = frame.copy()
                for c in contours:
                    cv2.drawContours(frame_contour , [c] , 0 , (0,255,0) , 5)
                if self.sum > self.confMotion:
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

            image = cv2.cvtColor(frame_contour , cv2.COLOR_BGR2RGB)
            FlippedImage = cv2.flip(image , 1)
            
            #QT format conversion
            converted = QImage(FlippedImage.data , FlippedImage.shape[1] , FlippedImage.shape[0] , QImage.Format_RGB888)
            Pic = converted.scaled(640,480,Qt.KeepAspectRatio)
            self.ImageUpdate.emit(Pic)
            original = gray
            end = time.time()
            self.fps = int(1/(end-start))

    def stop(self):
        self.threadActive = False
        self.quit()
        
    