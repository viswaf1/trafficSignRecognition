import numpy as np
import cv2



def highInvariantTreshold(inputImage):
    
    hsvImage = cv2.cvtColor(inputImage, cv2.COLOR_BGR2HSV_FULL)
    hslImage = cv2.cvtColor(inputImage, cv2.COLOR_BGR2HLS_FULL)
    
    treshLow1 = np.array([235, 0, 0], dtype=np.uint8)
    treshHigh1 = np.array([255, 255, 255], dtype=np.uint8)
    img1 = cv2.inRange(hsvImage, treshLow1, treshHigh1)
    
    treshLow1 = np.array([0, 40, 0], dtype=np.uint8)
    treshHigh1 = np.array([255, 255, 255], dtype=np.uint8)
    img2 = cv2.inRange(hsvImage, treshLow1, treshHigh1)
    
    treshLow1 = np.array([0, 0, 30], dtype=np.uint8)
    treshHigh1 = np.array([255, 255, 230], dtype=np.uint8)
    img3 = cv2.inRange(hsvImage, treshLow1, treshHigh1)
    
    treshLow2 = np.array([0, 0, 0])
    treshHigh2 = np.array([10, 255, 255])
    img4 = cv2.inRange(hsvImage, treshLow2, treshHigh2)
    
#     treshLow2 = np.array([0, 0, 150])
#     treshHigh2 = np.array([255, 255, 255])
#     img6 = cv2.inRange(hsvImage, treshLow2, treshHigh2)
    
    cv2.bitwise_or(img1,img4,img1)
    cv2.bitwise_and(img1,img2,img1)
    cv2.bitwise_and(img1,img3,img1)
    #cv2.bitwise_or(img1,img6,img1)
    
    kernel = np.ones((2,2),np.uint8)
    closing = cv2.morphologyEx(img1,cv2.MORPH_CLOSE,kernel, iterations = 2)
    img1 = cv2.morphologyEx(closing,cv2.MORPH_OPEN,kernel, iterations = 2)
    #img1 = cv2.dilate(opening,kernel,iterations=3)
    
    width = np.size(img1, 1)
    height = np.size(img1, 0)
    img1 = growRegion(img1,(width/2,height/2) )
    treshImage = img1

    return treshImage



def growRegion(img, seed):
    
    xS = seed[0]
    yS = seed[1]
    
    width = np.size(img, 1)
    height = np.size(img, 0)
    
    seeds = getSeeds((xS, yS), width, height, img)

    newImg = np.zeros((height,width,1), np.uint8)

    for (x,y) in seeds:            
        children = []
        #newImg[x][y] = 255
        
        while 1:
            succ = getsuccessors((x,y), width, height)
            
            for eachSucc in succ:
                if(img[eachSucc[1],eachSucc[0]] > 0):                
                    children.append(eachSucc)
                    img[eachSucc[1],eachSucc[0]] = 0
            if len(children) > 0:
                (x,y) = children[-1]
                newImg[y][x] = 255
                del(children[-1])
            else:
                break
        
    return newImg

def getSeeds((x,y), xLim, yLim, img):
    succ = []
    for i in range(x,xLim):
        if (img[y][i] > 0):
            succ.append((i,y))
            break
    for i in range(x,0,-1):
        if (img[y][i] > 0):
            succ.append((i,y))
            break
    for i in range(y,yLim):
        if (img[y][x] > 0):
            succ.append((x,i))
            break
    for i in range(y,0,-1):
        if (img[y][x] > 0):
            succ.append((x,i))
            break
    xNew = x
    yNew = y
    while 1:
        if xNew < xLim and yNew < yLim and xNew > 0 and  yNew > 0:
            if (img[yNew][xNew] > 0):
                succ.append((xNew,yNew))
                break
        else:
            break
        xNew = xNew + 1
        yNew = yNew + 1
        
    xNew = x
    yNew = y
    while 1:
        if xNew < xLim and yNew < yLim and xNew > 0 and  yNew > 0:
            if (img[yNew][xNew] > 0):
                succ.append((xNew,yNew))
                break
        else:
            break
        xNew = xNew - 1
        yNew = yNew - 1
        
    xNew = x
    yNew = y
    while 1:
        if xNew < xLim and yNew < yLim and xNew > 0 and  yNew > 0:
            if (img[yNew][xNew] > 0):
                succ.append((xNew,yNew))
                break
        else:
            break
        xNew = xNew + 1
        yNew = yNew - 1
 
    xNew = x
    yNew = y
    while 1:
        if xNew < xLim and yNew < yLim and xNew > 0 and  yNew > 0:
            if (img[yNew][xNew] > 0):
                succ.append((xNew,yNew))
                break
        else:
            break
        xNew = xNew - 1
        yNew = yNew + 1
 
            
    return succ
    
def getsuccessors((x,y), xLim, yLim):
    succ = []
    
    steps = [-1,0,1]
    for i in steps:
        for j in steps:
            if not (i == 0 and j == 0):
                if x+i > 0 and y+j > 0 and x+i < xLim and y+j < yLim:
                    succ.append((x+i,y+j))
        
    return succ
    
    
def imToArray(im):
    im = cv2.resize(im, (35,35) )
    arr = im.ravel()
    BinArr = arr
    BinArr = arr > 0
    BinArr = BinArr.astype(int)
    return BinArr
    
    