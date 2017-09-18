# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 08:45:09 2017

@author: dupres
"""

def selective_inc_sort(pMatrix):
    temp = 0
    pIndice = 0
    for i in xrange(len(pMatrix)):
        pIndice = i
        for j in range( i, len(pMatrix)):
            if pMatrix[pIndice] > pMatrix[j] :
                pIndice = j
        temp=pMatrix[i]
        pMatrix[i]=pMatrix[pIndice]
        pMatrix[pIndice]=temp
    return pMatrix

def selective_desc_sort(pMatrix):
    temp = 0
    pIndice = 0
    for i in xrange(len(pMatrix)):
        pIndice = i
        for j in range( i, len(pMatrix)):
            if pMatrix[pIndice] < pMatrix[j] :
                pIndice = j
        temp=pMatrix[i]
        pMatrix[i]=pMatrix[pIndice]
        pMatrix[pIndice]=temp
    return pMatrix




print (selective_inc_sort([2,3,4,59,7,5,10,15,7,1,3,3,9]))