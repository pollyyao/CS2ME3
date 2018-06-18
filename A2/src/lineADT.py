## @file line.py
#  @title lineADT
#  @author Polly Yao
#  @date 2/19/2017

## @brief This class represents a line
#  @details This class represents a point as p1 and p2 define two point of a line


import math
import pointADT


## @brief Constructor for LineT
#  @param p1 a point at the front of the line
#  @param p2 a point at the back of the line
class LineT:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
## @brief This function receives p1 from the constructor
#  @return the beginning point of the line
    def beg(self):
        
        return (self.p1)

## @brief This function receives p2 from the constructor
#  @return the back point of the line
    def end(self):
        return (self.p2)

## @brief This function calculates the length of the line
#  @return the length
    def len(self):
        result = (self.p1).dist(self.p2)
        return result


## @brief This function calculates the midpoint of the line
#  @return the a midpoint(PointT)
    def mdpt(self):
        
        a0 = (self.p1.xcrd())
        a1 = (self.p2.xcrd())
        af = (a0 + a1)/2

        b0 = (self.p1.ycrd())
        b1 = (self.p2.ycrd())
        bf = (b0 + b1)/2

        res = pointADT.PointT(af, bf)

        return res
## @brief This function rotates front point and back point of the line
#  @param phi a radian
    def rot(self, phi):
        (self.p1).rot(phi)
        (self.p2).rot(phi)
        
