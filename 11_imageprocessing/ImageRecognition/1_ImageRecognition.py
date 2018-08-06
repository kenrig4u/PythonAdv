# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 13:57:26 2018

@author: SilverDoe
"""

from PIL import Image as pil
import numpy as np
from statistics import mean
from collections import Counter

import matplotlib.pyplot as plt
import time
     
'''============================= creating sample data ========================='''
# plot the images that needs to be processed        
i = pil.open('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\images\\numbers\\0.1.png')
iar = np.array(i)
i2 = pil.open('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\images\\numbers\\y0.4.png')
iar2 = np.array(i2)
i3 = pil.open('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\images\\numbers\\y0.5.png')
iar3 = np.array(i3)
i4 = pil.open('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\images\\sentdex.png')
iar4 = np.array(i4)


fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()

# userdefined function for normalizing the data
def threshold(imageArray):

    balanceAr = []
    newAr = imageArray
    #from statistics import mean
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum)

    balance = mean(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr


# getting the normalized data from the user defined function
iar = threshold(iar)
iar2 = threshold(iar2)
iar3 = threshold(iar3)
iar4 = threshold(iar4)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)


plt.show()

# Saving the numpy array into a text file for later use as pattern
def createExamples():
    numberArrayExamples = open('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\numArEx.txt','a')
    numbersWeHave = range(1,10)
    for eachNum in numbersWeHave:
        #print eachNum
        for furtherNum in numbersWeHave:
            # you could also literally add it *.1 and have it create
            # an actual float, but, since in the end we are going
            # to use it as a string, this way will work.
            print(str(eachNum)+'.'+str(furtherNum))
            imgFilePath = 'E:/Documents/PythonProjects/1_Basics/DataForFiles/images/numbers/'+str(eachNum)+'.'+str(furtherNum)+'.png'
            ei = pil.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            print(eiarl)
            lineToWrite = str(eachNum)+'::'+eiarl+'\n'
            numberArrayExamples.write(lineToWrite)

createExamples()



def whatNumIsThis(filePath):

    matchedAr = []
    loadExamps = open('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')
    
    i = pil.open(filePath)
    i.resize((8,8))
    iar = np.array(i)
    print(iar.shape)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            
            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')

            x = 0

            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                x+=1
        except Exception as e:
            print(str(e))
                
    print(matchedAr)
    x = Counter(matchedAr)
    print(x)
    print(x[0])

whatNumIsThis('E:/Documents/PythonProjects/1_Basics/DataForFiles/images/testimage2.png')


            
            
            
            
            
            
            
            
            
            
            

