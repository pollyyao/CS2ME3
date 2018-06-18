## @file Statistics.py
#  @title Statistics
#  @author Polly Yao
#  @date 1/28/2017

## @brief This module has three methods(average, stdDev, rank) for CircleADT.py
#  @details This module takes in a list of instances of circles

import CircleADT
import numpy as np


## @brief This method calculate the average of radius of a list circle instances
#  @param thelist is a list of instance of circles
#  @return the average of all the radius
def average(thelist):
    ans = []
    
    for element in thelist:
        ans.append(element[2])
       
    avg = np.average(ans)    
    return (avg)


## @brief This method calculate the standard deviation of radius of a list circle instances
#  @param thelist is a list of instance of circles
#  @return the standard deviation of all the radius
def stdDev(thelist):
    ans = []
    for element in thelist:
        i = ans.append(element[2])        

    stdD = np.std(ans)
    return (stdD)


## @brief This method rank a list of instances CircleT by radius
#  @param thelist is a list of instance of circles
#  @assumption if there are element duplicates in the list, the function will remove all the duplicates and leave only one copy of that element
#  @return the list ranked by radius
def rank(thelist):
    array = []
    arrai = []
    arraa = []
    for element in thelist:
        array.append(element[2])
        arrai.append(element[2])


    arrayR = []
    sawA = set()
    for element in array:
        if element not in sawA:
            arrayR.append(element)
            sawA.add(element)

  
    arraiR = []
    sawB = set()
    for element in arrai:
        if element not in sawB:
            arraiR.append(element)
            sawB.add(element)

  
    for i in range(len(arrayR)):
        for j in range(i+1, len(arrayR)):
            if arrayR[j] > arrayR[i]:
                arrayR[j], arrayR[i] = arrayR[i], arrayR[j]

    
    for element in arrayR:
        if (element in arraiR):
            c = arraiR.index(element)
            arraa.append(c+1)



    return arraa

        
