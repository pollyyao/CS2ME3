## @file pointADT.py
#  @title pointADT
#  @author Polly Yao
#  @date 2/19/2017

## @brief This class represents a point
#  @details This class represents a point as x and y define the x and y corrdinates of a point


import math

## @brief Constructor for PointT
#  @param x coordinate of a point
#  @param y coordinate of a point
class PointT:
    def __init__(self, x, y):
        self.x = x
        self.y = y

## @brief This function receives x from the constructor
#  @return x coordinate of the circle
    def xcrd(self):
        return (self.x)

## @brief This function receives y from the constructor
#  @return y coordinate of the circle
    def ycrd(self):
        return (self.y)

## @brief This function calculates the distance of two points
#  @param p is another instance of point
#  @return distance between two point
    def dist(self, p):
        A = (self.x - p.x)**2
        B = (self.y - p.y)**2
        result = math.sqrt(A+B)
        return result

## @brief This function rotates the x and y coordiantes
#  @param phi a radian

    def rot(self, phi):
        cx = (math.cos(phi)*self.x) + (-math.sin(phi)*self.y)
        cy = (math.sin(phi)*self.x) + (math.cos(phi)*self.y)
        self.x = cx
        self.y = cy

        
        
