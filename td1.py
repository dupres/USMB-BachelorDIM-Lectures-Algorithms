# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 09:50:14 2017

@author: dupres
"""

import random

##
#Small function describing an input list
def list_analysis(pList):
    
    #Variables initialization
    pSum = 0
    pPositiveCount = 0
    pNegativeCount = 0   
    
    for i in xrange(len(pList)):
        if pList[i]>0:
            pPositiveCount = pPositiveCount +1
        else:
            pNegativeCount = pNegativeCount +1
        pSum = pSum + pList[i]
    pAverage = pSum / i
    print('There is '+str(pPositiveCount)+' positive values and '+str(pNegativeCount)+' negative values in this array. The average is '+str(pAverage)+'.')


##
#Small function giving the maximum value of a list
def list_max(pList):
    #Variables initialization
    pMaxValue = -10000000
    for i in pList:
        if pMaxValue<i:
            pMaxValue = i
    print('MaxValue is '+str(pMaxValue))

#Random input list
pList = []
pListLen = random.randint(50,100)
for i in xrange(pListLen):
    pList.append(random.randint(-100,100))

list_max(pList)

