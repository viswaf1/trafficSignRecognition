import numpy as np
import cv2
import os
import csv
import util
from util import FNAME, CLASSID
from imageDataSet import imageDataSet
import preProcess
import sliderTresh
import Data

def makeDataSet():

    #stop sign
    dataSetList = ['00013', '00014', '00015', '00017', '00019']
        
    #20 sign
    #dataset = '00000'
    
    currentLoc = os.getcwd()+'/'
    dataloc = '../GTSRB/Final_Training/Images/'
    finalData = Data.Data()
    
    for dataset in dataSetList:
    
        fileList = os.listdir(currentLoc+dataloc+dataset+'/')
        
        imageFiles = []
        fileLoc = currentLoc+dataloc+dataset+'/'
        annFile = "GT-"+dataset+".csv"
        
        annData = []
        with open(fileLoc+annFile, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            count = 0
            for row in spamreader:
                if(count > 0):
                    annData.append(row)
                count = count + 1
        
        imData = imageDataSet()
        for eachAnn in annData:
            if(eachAnn[FNAME] in fileList):
                img = cv2.imread(fileLoc+eachAnn[FNAME], cv2.IMREAD_COLOR)
                imData.addImgData(img, eachAnn)
        
        
        treshDest = "../outImages/"
        for eachData in imData.Data:
            treshImg = preProcess.highInvariantTreshold(eachData[0])
            imArr = preProcess.imToArray(treshImg)
            binArr = imArr > 0
            binArr = binArr.astype(int)
            if float(sum(binArr))/float(binArr.size) >= 0.1: 
                ann = eachData[1]
                finalData.addRow(ann[CLASSID], imArr, ann)
                
                if not os.path.exists(treshDest+dataset):
                    os.makedirs(treshDest+dataset)
                cv2.imwrite(treshDest+dataset+"/"+eachData[1][FNAME], treshImg)
            
        print "dataset "+dataset+" Done!"
        
    #     cv2.imshow('img',treshImg)
    #     cv2.waitKey(0)

    return finalData

def makeTestDataSet():
    dataSetList = ['13', '14', '15', '17', '19']
    testData = Data.Data()
    currentLoc = os.getcwd()+'/'
    dataloc = '../GTSRB_TEST/Online-Test/Images/'
    
    fileList = os.listdir(currentLoc+dataloc+'/')
        
    imageFiles = []
    fileLoc = currentLoc+dataloc+'/'
    annFile = "GT-online_test.csv"
    
    annData = []
    with open(fileLoc+annFile, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        count = 0
        for row in spamreader:
            if(count > 0):
                annData.append(row)
            count = count + 1
    
    imData = imageDataSet()
    for eachAnn in annData:
        if(eachAnn[FNAME] in fileList) and eachAnn[CLASSID] in dataSetList:
            img = cv2.imread(fileLoc+eachAnn[FNAME], cv2.IMREAD_COLOR)
            imData.addImgData(img, eachAnn)
    
    
    treshDest = "../outImages/"
    for eachData in imData.Data:
        treshImg = preProcess.highInvariantTreshold(eachData[0])
        imArr = preProcess.imToArray(treshImg)
        binArr = imArr > 0
        binArr = binArr.astype(int)
        if float(sum(binArr))/float(binArr.size) >= 0.1:
            ann = eachData[1]
            testData.addRow(ann[CLASSID], imArr, ann)
            
            if not os.path.exists(treshDest+"testImages"):
                os.makedirs(treshDest+"testImages")
            cv2.imwrite(treshDest+"testImages"+"/"+eachData[1][FNAME], treshImg)
            
    return testData

