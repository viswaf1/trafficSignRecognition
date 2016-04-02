import numpy

def buildSVM(data,r0,C,epochs, kernelType):
    w = numpy.array([0] * len(data.data[0]['x']))
    t = 0
    for eachEpoch in range(epochs):
        data.shuffleData()
        for row in data.data:
            rate = (r0)/(1+((r0*t)/C))
            #if(row['y']*numpy.dot(numpy.transpose(w),row['x']) <= 1):
            if(row['y']*kernel(w,row,kernelType) <= 1 ):
                delJ = w - (C*(row['y']*row['x']))
            else:
                delJ = w
            
            w = w - (rate*(delJ))
            t = t + 1

    return w


def checkSVM(data,w):
    success = 0
    failure = 0
    for eachRow in data.data:
        if(eachRow['y'] == getSVMLabel(w, eachRow)):
            success = success + 1
        else:
            failure = failure + 1
    return (float(success)/float(success+failure))*100.0
        
def getSVMLabel(w,row, kernelType):
    #y = numpy.dot(numpy.transpose(w), row['x'])
    y = kernel(w,row,kernelType)
    if y > 0:
        signY = 1
    else:
        signY= -1
    
    return signY
        

def kernel(w,row,kernelType):
    if kernelType == "linear":
        y = numpy.dot(numpy.transpose(w), row['x'])
#         print y
#         print numpy.tanh(y)
#         print"---------------"
        return y   
    
    if kernelType == "sigmoid":
#         print numpy.dot(numpy.transpose(w), row['x'])
        y = numpy.tanh(0.0001*numpy.dot(numpy.transpose(w), row['x']) - 0.85)
#         print y
#         print "-----------"
        return y
    
    if kernelType == "polynomial":
        y = (1*numpy.dot(numpy.transpose(w), row['x']) + 2)**3
#         print y
        return y
    





