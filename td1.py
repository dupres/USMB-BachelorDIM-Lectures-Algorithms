# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 09:50:14 2017
@author: dupres
"""

import random
import numpy

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

##
#Creates a random boolean matrix with random limits between 2 and 10
def create_matrix():
    pWidth = random.randint(2,10)
    pHeight = random.randint(2,10)
    
    pMatrix = numpy.zeros((pWidth,pHeight))
    
    for i in xrange(pWidth):
        for j in xrange(pHeight):
            pMatrix[i,j] = random.randint(0,1)
    return pMatrix

##
#Small function giving the boundaries of a matrix
#@param input matrix : the matrix to analyze
#throws an exception (ValueError) on an empty matrix
def matrix_boundaries(pMatrix):
    #First check : if matrix width or height is 0
    if len(pMatrix) == 0:
        raise ValueError('Matrix length should not be 0')
    elif len(pMatrix[0]) == 0:
        raise ValueError('Matrix length should not be 0')
    return len(pMatrix), len(pMatrix[0])

#-------------------------------------------------------------------

pBox = create_matrix()

print(pBox)
print(matrix_boundaries(pBox))