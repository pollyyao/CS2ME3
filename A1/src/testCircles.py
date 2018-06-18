## @file testCircles.py
#  @title test
#  @author Polly Yao
#  @date 1/28/2017

## @brief This module includes all the test cases for CircleADT.py and Statistics.py


import CircleADT
import Statistics


## @brief create the Circle a
a = CircleADT.CircleT(3, 4, 1)


## @brief output the x coordinate of the circle
print(a.xcoord())


## @brief output the y coordinate of the circle
print(a.ycoord())


## @brief output the radius of the circle
print(a.radius())


## @brief output the area of the circle
print(a.area())


## @brief output the circumference of the circle
print(a.circumference())


## @brief check if the circle is inside the box(1, 1, 5, 6)
#  @detail output True
print(a.insideBox(1, 1, 5, 6))


## @brief check if the circle is inside the box(2, 1, 5, 6)
#  @detail output False
print(a.insideBox(2, 1, 5, 6))


## @brief create the Circle b
b = CircleADT.CircleT(6, 3, 3)


## @brief Test if Circle a and Circle b intersect
## @detail output True
print(a.intersect(b))


## @brief create the Circle c
c = CircleADT.CircleT(6, 2, 1)


## @brief Test if Circle a and Circle c intersect
## @detail output False
print(a.intersect(c))


## @brief create the Circle d
d = CircleADT.CircleT(5, 3, 1.24)


## @brief Test if circle a and cirlce d intersect
#  @detail Circle d intersect with circle at one point(x == 4)
#  @detail output True
print(a.intersect(d))


## brief scale radius by a factor 4
a.scale(4.0)


## brief output the radius after scale
print(a.radius())


## brief move x and y coordinate of the circle by (8, 6)
a.translate(8, 6)


## brief output the x and y coordinate after translate
print(a.xcoord(), a.ycoord())


## @brief create the Circle e
e = CircleADT.CircleT(2, 3, 2)


## @brief create the Circle f
f = CircleADT.CircleT(4, 4, 1)


## @brief create the Circle g
g = CircleADT.CircleT(6, 5, 4)


## @brief create an array with circle e, f, g
array = [[e.x,e.y,e.r], [f.x,f.y,f.r], [g.x, g.y, g.r]]


## brief output the average radius 
print(Statistics.average(array))


## brief output the standard deviation
print(Statistics.stdDev(array))


## brief output a ranked list of radius
print(Statistics.rank(array))


## @brief create the Circle h
h = CircleADT.CircleT(3, 5, 2)

## @brief create an array with circle e, f, g, h, contain duplicates(e.r, h.r)
arr = [[e.x,e.y,e.r], [f.x,f.y,f.r], [g.x, g.y, g.r], [h.x, h.y, h.r]]


## @brief output a ranked list of radius with duplicates(two 2)
#  @detail The rank function will remove one of the 2
print(Statistics.rank(arr))
      

