## @file CircleADT.py
#  @title CircleADT
#  @author Polly Yao
#  @date 1/28/2017

## @brief This class represents a circle
#  @details This class represents a circle as x and y values define the centre of the circle
#   and r defines the radius of the circle

import math


## @brief Constructor for CircleT
#  @param x and y as the coordinate for the centre of the circle
#  @param r as the radius of the circle
class CircleT:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


## @brief This function receives the x coordinate from the constructor
#  @return x coordinate of the circle
    def xcoord(self):
        return (self.x)


## @brief This function receives the y coordinate from the constructor
#  @return y coordinate of the circle
    def ycoord(self):
        return (self.y)


## @brief This function receives the radius from the constructor
#  @return radius of the circle
    def radius(self):
        return (self.r)


## @brief This function calculates the area of the circle
#  @return the area of the circle
    def area(self):
        a = (math.pi)*((self.r)**2)
        return a


## @brief This function calculates the circumerence of the circle
#  @return the circumerence of the circle
    def circumference(self):
        c = 2*(math.pi)*(self.r)
        return c


## @brief This function checks if a circle is inside a box.
#  @details This function takes in the (bx, by, w, h) coordinate of a rectangle box
#  @param bx is the x coordinate of the left side of a box, by is the y coordinate of the top of the box
#  @param w is the width of the box and h is the height of the box
#  @return True if the circle is inside the box, False if it is not
    def insideBox(self, bx, by, w, h):
        
        rightx = bx + w
        topy = by + h
        leftc = self.x - self.r
        rightc = self.x + self.r
        bottomc = self.y - self.r
        topc = self.y + self.r

        if (leftc > bx and rightc < rightx) and (bottomc > by and topc < topy):
            return True

        else:
            return False



## @brief This function checks if two circles intersect
#  @details This function takes in another circle c
#  @details The two  circles intersect if the sum of two radius is greater and equal to the sum of differences between x and y coordinate of two circles 
#  @param c is the second instance of CircleT
#  @return True if two circles intersect, False if they do not
    def intersect(self, c):
        distance = math.sqrt((c.y - self.y)**2 +(c.x - self.x)**2)
        radii = c.r + self.r

        if (radii >= distance):
            return True

        else:
            return False
        

## @brief This function change the radius by a factor k
#  @param k is the a float that stretch or shorten the radius
    def scale(self, k):
        assert type(k) == float
        self.r = self.r * k


## @brief This function move the circle up around
#  @param dx moves the x coordinate up or down
#  @param dy moves the y coordinate left or right
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
