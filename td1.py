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
    #Analysis
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
#@param input list : a list to analyze
#throws an exception (ValueError) on an empty list
def list_max(pList):
    #First check
    if len(pList)==0:
        raise ValueError('List length should not be 0')
    #Variables initialization
    pMaxValue = pList[0]
    pMaxIndex = 0
    #Check
    for i in xrange(len(pList)):
        if pMaxValue<pList[i]:
            pMaxValue = pList[i]
            pMaxIndex = i
    print('MaxValue is '+str(pMaxValue)+' at index '+str(pMaxIndex))
    return pMaxValue, pMaxIndex
    
##
#Small function that reverse a list
#@param input list : a lis to reverse
#throws an exception (ValueError) on an empty list
def list_reverse(pList):
    #First check
    if len(pList)==0:
        raise ValueError('List length should not be 0')
    #Reverse
    for i in xrange(len(pList)/2):
        temp = pList[i]
        pList[i] = pList[len(pList)-i-1]
        pList[len(pList)-i-1] = temp
    return pList
    
##
#Small function that creates a random list with between 50 and 100 values
#between -100 and 100
def create_list():
    pList = []
    pListLen = random.randint(50,100)
    for i in xrange(pListLen):
        pList.append(random.randint(-100,100))
    return pList
        
#print('Max value is '+str(list_max(pList)))
pList = create_list()
print(pList)
print(list_reverse(pList))