# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 09:50:14 2017
@author: dupres
"""

import random
import numpy

##
#Small function describing an input list
def average_above_zero(pList):
    #Variables initialization
    pSum = 0
    pPositiveCount = 0
    pNegativeCount = 0   
    if len(pList)==0:
        raise ValueError('List length should not be 0')
    #Analysis
    for i in xrange(len(pList)):
        if pList[i]>0:
            pPositiveCount = pPositiveCount +1
        else:
            pNegativeCount = pNegativeCount +1
        pSum = pSum + pList[i]
    pAverage = pSum / i
    print('There is '+str(pPositiveCount)+' positive values and '+str(pNegativeCount)+' negative values in this array. The average is '+str(pAverage)+'.')
    return [pPositiveCount,pNegativeCount,pAverage]

##
#Small function giving the maximum value of a list
#@param input list : a list to analyze
#throws an exception (ValueError) on an empty list
def max_value(pList):
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
def reverse_table(pList):
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
    
    pMatrix = numpy.zeros((pWidth,pHeight),dtype=int)
    
    for i in xrange(pWidth):
        for j in xrange(pHeight):
            pMatrix[i,j] = random.randint(0,1)
    return pMatrix

##
#Creates an empty boolean matrix with random limits between 2 and 10
#and with inside a 3*3 square made of true values
def create_matrixWithSquare():
    pWidth = random.randint(3,10)
    pHeight = random.randint(3,10)
    pSquarePosX = random.randint(0,pWidth-3)
    pSquarePosY = random.randint(0,pHeight-3)
    pSquareDim = 3
    
    pMatrix = numpy.zeros((pWidth,pHeight),dtype=int)
    for i in xrange(pSquareDim):
        for j in xrange(pSquareDim):
            pMatrix[pSquarePosX + i,pSquarePosY + j] = 1
    return pMatrix
    
##
#Small function giving the dimensions of a matrix
#@param input matrix : the matrix to analyze
#throws an exception (ValueError) on an empty matrix
def matrix_dimensions(pMatrix):
    #First check : if matrix width or height is 0
    if len(pMatrix) == 0:
        raise ValueError('Matrix length should not be 0')
    elif len(pMatrix[0]) == 0:
        raise ValueError('Matrix length should not be 0')
    return len(pMatrix), len(pMatrix[0])

##
#Finds the boundaries of a square inside a matrix
#@param input matrix : the matrix to analyze
#throws an exception (ValueError) on an empty matrix
def roi_bbox(pMatrix):
    #First check : if matrix width or height is 0
    if len(pMatrix) == 0:
        raise ValueError('Matrix should exists')
    elif len(pMatrix[0]) == 0:
        raise ValueError('Matrix length should not be 0')
    if np.sum(pMatrix) == 0:
        raise ValueError('Matrix should not be empty')
    #Variables initialization
    pLeftTopBoundary = [0,0]
    pRightBottomBoundary = [0,0]
    pWidth = matrix_dimensions(pMatrix)[0]
    pHeight = matrix_dimensions(pMatrix)[1]
    coordXTopLeft = 0
    coordYTopLeft = 0
    coordXBottomRight = 0
    coordYBottomRight = 0
    
    #Calculation
    i=0
    j=0
    while i < pWidth:
        while j<pHeight:
            if coordXTopLeft = 0 and pMatrix[i,j]=1:
                coordXTopLeft = i
            if coordYTopLeft = 0 and pMatrix[i,j]=1:
                coordYTopLeft = j
            i=i+1
            j=j+1
            if coordXTopLeft != 0 and coordYTopLeft != 0:
                i = pWidth
                j = pHeight
    i=pWidth
    j=pHeight
    while i > 0:
        while j > 0:
            if coordXBottomRight = 0 and pMatrix[i,j]=1:
                coordXBottomRight = i
            if coordYBottomRight = 0 and pMatrix[i,j]=1:
                coordYBottomRight = j
            i=i-1
            j=j-1
            if coordXBottomRight != 0 and coordYBottomRight != 0:
                i = 0
                j = 0
    
    # while i < pWidth:
        # while j < pHeight:
            # if pMatrix[i,j]<>0 and pLeftTopBoundary[0] == 0 and pLeftTopBoundary[1] == 0:
                # pLeftTopBoundary = [i,j]
            # if pMatrix[pWidth-i-1,pHeight-j-1]<>0 and pRightBottomBoundary[0] == 0 and pRightBottomBoundary[1] == 0:
                # pRightBottomBoundary = [pWidth-i-1,pHeight-j-1]
            # j=j+1
        # i=i+1
    
    return np.array([[coordXBottomRight,coordYBottomRight], [coordXTopLeft, coordYTopLeft]])

##
#Creates a random empty char matrix between 2 and 10 columns and rows
def create_charmatrix():
    pWidth = random.randint(2,10)
    pHeight = random.randint(2,10)
    pChar = numpy.chararray((pWidth,pHeight))
    #Empty pChar
    for i in xrange(pWidth):
        for j in xrange(pHeight):
            pChar[i,j] = ''
    print(pChar)
    return pChar

##
#Fills an input char matrix with an input number of 'X'
def random_fill_sparse(pCharmatrix,pNumberOfFills):
    print(pNumberOfFills)
    for i in xrange(pNumberOfFills):
        x = random.randint(0,matrix_dimensions(pCharmatrix)[0]-1)
        y = random.randint(0,matrix_dimensions(pCharmatrix)[1]-1)
        while pCharmatrix[x,y] <> '':
            x = random.randint(0,matrix_dimensions(pCharmatrix)[0]-1)
            y = random.randint(0,matrix_dimensions(pCharmatrix)[1]-1)
        pCharmatrix[x,y] = 'X'
    return pCharmatrix

##
#Removes whitespaces in a string
#@param input string : the string to check
def remove_whitespace(pString):
    pLength = len(pString)
    i = 0
    while i < pLength :
        if pString[i] == ' ':
            pString = pString[0:i] + pString[i+1:len(pString)]
            pLength = pLength - 1
        i = i+1
    return pString


#-------------------------------------------------------------------

print(remove_whitespaces("Ceci est une phrase avec plein d'espaces."))