#Author:
# Teja
# University of Utah
# Fall 2015
from collections import Counter
import numpy
from random import shuffle
from numpy.testing.utils import tempdir

class Data:
    """class to store data"""
    def __init__(self):
        self.data = []
        self.allLabels = []

    def addRow(self, label, inArr, ann):
        rowDict = {}
        xVal = []
        rowDict['y'] = label
        rowDict['x'] = inArr
        rowDict['ann'] = ann
        self.data.append(rowDict)
        if label not in self.allLabels:
            self.allLabels.append(label)
        
    def shuffleData(self):
        newData = []
        ind = range(len(self.data))
        shuffle(ind)
        for i in ind:
            newData.append(self.data[i])
        self.data = newData
        
    def getDataForModel(self, label):
        newData = Data()
        for eachRow in self.data:
            tempdict = {}
            tempdict['x'] = eachRow['x']
            tempdict['ann'] = eachRow['ann']
            if eachRow['y'] == label:
                tempdict['y'] = 1
            else:
                tempdict['y'] = -1   
            newData.data.append(tempdict)
        return newData
    
    def getDataWithLabel(self, label):
        newData = Data()
        for eachRow in self.data:
            if eachRow['y'] == label:
                tempdict = {}
                tempdict['x'] = eachRow['x']
                tempdict['ann'] = eachRow['ann']
                tempdict['y'] = eachRow['y']   
                newData.data.append(tempdict)
        return newData 
        

    