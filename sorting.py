# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 08:45:09 2017

@author: dupres
"""

# b) The number of iterations does not depend on the vector content.
# The number of iterations is always based on the length of the input matrix.
# 
# For a matrix like [10,15,7,1,3,3,9], 
# 
# c) 28 iterations are required
# 
# d) 7 permutations are applied
# 
# e) 28 comparisons are applied
# 
# f) This algorithm is one of the simplest
#  

import random
import numpy

def create_random_array(size):
    pArray = numpy.zeros(size)
    for i in xrange(size):
        pArray[i] = random.randint(1,99)
    return pArray

def selective_sort(pMatrix, pOrder):
    temp = 0
    pIndice = 0
    
    nbPermut = 0
    nbComp = 0
    
    for i in xrange(len(pMatrix)):
        pIndice = i
        for j in range( i, len(pMatrix)):
            nbComp = nbComp+1
            if pOrder == "asc":
                if pMatrix[pIndice] > pMatrix[j] :
                    pIndice = j
            else:
                if pMatrix[pIndice] < pMatrix[j] :
                    pIndice = j
        temp=pMatrix[i]
        pMatrix[i]=pMatrix[pIndice]
        pMatrix[pIndice]=temp
        nbPermut = nbPermut+1
        
    print nbComp,nbPermut        
        
    return pMatrix

def bubble_sort(pMatrix,pOrder):
    temp = 0
    for i in xrange(len(pMatrix)):
        for j in xrange(len(pMatrix)-1):
            if pOrder == 'asc':
                if pMatrix[j]>pMatrix[j+1]:
                    temp = pMatrix[j]
                    pMatrix[j]=pMatrix[j+1]
                    pMatrix[j+1]=temp
            else:
                if pMatrix[j]<pMatrix[j+1]:
                    temp = pMatrix[j]
                    pMatrix[j]=pMatrix[j+1]
                    pMatrix[j+1]=temp
    return pMatrix
