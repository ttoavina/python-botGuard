from PyQt5 import QtGui
from utils.detector import CamWorker


class MainController:
    
    def __init__(self , view) -> None:
        self.view = view
    
 
    def load(self):
        self.worker1 = CamWorker()
        self.worker1.start()
        self.worker1.ImageUpdate.connect(self.imageUpdateSlot)

    def imageUpdateSlot(self , image):
        self.view.mainCam.setPixmap(QtGui.QPixmap.fromImage(image))
        self.view.fpsNumber.setDigitCount(self.worker1.fps)
        self.view.intrusionNumber.setDigitCount(self.worker1.sum)