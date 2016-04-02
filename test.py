import numpy as np
import cv2
import os

dataset = '00014'
currentLoc = os.getcwd()+'/'
dataloc = '../GTSRB/Final_Training/Images/'

fileList = os.listdir(currentLoc+dataloc+dataset+'/')

imageFiles = []
annFile = ""
for eachFile in fileList:
    filecomp = eachFile.split('.')
    if len(filecomp) > 0:
        if(filecomp[1] == 'ppm'):
            imageFiles.append(eachFile)
        if(filecomp[1] == 'csv'):
            annFile = eachFile
            
print annFile

dirPath = currentLoc+dataloc+dataset+'/'
img = cv2.imread(dirPath+imageFiles[28],cv2.IMREAD_COLOR)
cv2.imshow('image',img)
cv2.waitKey(0) 


