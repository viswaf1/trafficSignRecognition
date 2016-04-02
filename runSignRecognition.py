import readImgData
import cv2
import numpy as np
import svmTrainer
import pickle
from xcb.glx import CurrentDrawableError

svmData = readImgData.makeDataSet()
pickle.dump(svmData, open('processedData', 'wb'))
testSvmData = readImgData.makeTestDataSet()
pickle.dump(testSvmData, open('processedTestData', 'wb'))

# svmData = pickle.load(open('processedData', 'rb'))
# testSvmData = pickle.load(open('processedTestData', 'rb'))
print svmData.allLabels
print testSvmData.allLabels



models = []
modelData = []
kernelType = "linear"
for label in svmData.allLabels:
    cPlus = 0
    cMinus = 0
    currentData = svmData.getDataForModel(label)
    modelData.append(currentData)
    for row in currentData.data:
        if row['y'] == 1:
            cPlus = cPlus + 1
        else:
            cMinus = cMinus + 1
    print str(label) + " : " + str(cMinus) + " out of " + str(cPlus + cMinus)
    
    w = svmTrainer.buildSVM(currentData, 0.5, 1, 100, kernelType)
    models.append((w, label))
    
for label in testSvmData.allLabels:
    labelData = testSvmData.getDataWithLabel(label)
    
    correct = 0
    wrong = 0
    partial = 0
    for eachRow in labelData.data:
        results = []
        for eachModel in models:
            result = svmTrainer.getSVMLabel(eachModel[0], eachRow, kernelType)
            results.append((eachModel[1],result))
        #print results
        partialFlag = 0
        correctFlag = 0
        correctCnt = 0
        for eachResult in results:
            if(eachResult[1] == 1):
                if(eachResult[0] == label):
                    correctFlag = 1
                correctCnt = correctCnt + 1
        if correctFlag == 1 and correctCnt == 1:
            correct = correct+1
        else:
            wrong = wrong + 1
        
            
    print " for class "+ str(label) +" correct : "+str(correct)+" wrong : "+str(wrong)+" accuracy : "+str(float(correct)/(float(correct+wrong))*100)
        
        