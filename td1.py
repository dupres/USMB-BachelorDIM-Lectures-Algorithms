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
    #First check
    if len(pList)==0:
        raise ValueError('List length should not be 0')
    #Variables initialization
    pMaxValue = pList[0]
    pMaxIndex = 0
    for i in xrange(len(pList)):
        if pMaxValue<pList[i]:
            pMaxValue = pList[i]
            pMaxIndex = i
    print('MaxValue is '+str(pMaxValue)+' at index '+str(pMaxIndex))
    return pMaxValue
#Random input list
pList = []
pListLen = random.randint(50,100)
for i in xrange(pListLen):
    pList.append(random.randint(-100,100))

print('Max value is '+str(list_max(pList)))

