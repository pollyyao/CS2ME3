## @file CircleADT.py
#  @title CircleADT
#  @author Polly Yao
#  @date 2/19/2017

## @brief This class represents a circle
#  @details This class represents a circle as cin define the centre of the circle
#   and rin defines the radius of the circle

import math

import pointADT

import lineADT

## @brief Constructor for CircleT
#  @param cin as the coordinate for the centre of the circle
#  @param rin as the radius of the circle
class CircleT:
    def __init__(self, cin, rin):
        self.cin = cin
        
        self.rin = rin

## @brief This function receives cin from the constructor
#  @return centre(PointT) of the circle
    def cen(self):
        return (self.cin)

## @brief This function receives the radius from the constructor
#  @return radius of the circle
    def rad(self):
        return (self.rin)

## @brief This function calculates the area of the circle
#  @return the area of the circle
    def area(self):
        area = (math.pi)*((self.rin)**2)
        return area

## @brief This function checks if two circles intersect
#  @details This function takes in another circle ci
#  @details The two  circles intersect if the sum of two radius is greater and equal to the sum of differences between x and y coordinate of two circles 
#  @param ci is the second instance of CircleT
#  @return True if two circles intersect, False if they do not
    def intersect(self, ci):
        distance = math.sqrt((ci.cin.y - self.cin.y)**2 + (ci.cin.x - self.cin.x)**2)
        radii = self.rin + ci.rin

        if (radii >= distance):
            return True

        else:
            return False

## @brief This function forms a line between two circles
#  @details This function takes in another circle ci
#  @return the line
    def connection(self, ci):
        out = lineADT.LineT(self.cin, ci.cen())
        return out

## @brief This function is built for the force function
#  @details This function takes in another circle x
#  @return a answer that is used by force function
    
    def counter(self, x):
        r = self.connection(x).len()
        b = (6.672*(10**-11))/r**2
        area = x.area()
        result = b * area
        return result

## @brief This function fcalculates the force between two circles
#  @details This function takes in a function counter
#  @return the force between two circles      
    def force(self, method):
        return (self.area() * method)
