import cv2
from util import *

class imageDataSet:
    
    def __init__(self):
        self.Data = []
        
    def addImgData(self, img, ann):
        for x in range(1,8):
            ann[x] = int(ann[x])
        newImg = img[ann[ROIY1]:ann[ROIY2], ann[ROIX1]:ann[ROIX2]].copy()
        #newImg = cv2.resize(newImg,(IMGW,IMGH))
        self.Data.append([newImg,ann])
        
    