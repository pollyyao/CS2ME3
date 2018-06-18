## @file testCircleDeque.py
#  @title testCircleDeque
#  @author Polly Yao
#  @date 2/19/2017


import unittest
from pointADT import *
from lineADT import *
from circleADT import *
from deque import *


class pointTests(unittest.TestCase):

    def setUp(self):
        self.point1 = PointT(1, 2)
        self.point2 = PointT(4, 3)

        
    def tearDown(self):
        self.point1 = None
        self.point2 = None

    def test_xcrd_are_equal(self):
        self.assertTrue(self.point1.xcrd() == 1)

    def test_ycrd_are_equal(self):
        self.assertTrue(self.point1.ycrd() == 2)

    def testdist(self):
        self.assertAlmostEqual(self.point1.dist(self.point2), 3.1622776601683795,  None, None, 0.1)
    
    def testrot(self):
        (self.point1).rot(30)
        
        self.assertAlmostEqual(self.point1.xcrd(), 2.130314698073308,  None, None, 0.1)
        self.assertAlmostEqual(self.point1.ycrd(), -0.6795287243176937,  None, None, 0.1)



class lineTests(unittest.TestCase):
    def setUp(self):
        point1 = PointT(1, 2)
        point2 = PointT(4, 3)

        self.line = LineT(point1, point2)

    def tearDown(self):
        self.line = None

    def testbeg(self):
        self.assertTrue(self.line.beg().x == 1)

    def testend(self):
        self.assertTrue(self.line.end().x == 4)

    def testline(self):
        self.assertAlmostEqual(self.line.len(), 3.1622776601683795,  None, None, 0.1)

    def testmdpt(self):
        self.assertAlmostEqual(self.line.mdpt().x, 2,  None, None, 0.1)       
        self.assertAlmostEqual(self.line.mdpt().y, 2,  None, None, 0.1)

    def testrot(self):
        (self.line).rot(60)
        
        self.assertAlmostEqual(self.line.beg().x, -0.34279173821072295,  None, None, 0.1)
        self.assertAlmostEqual(self.line.beg().y, -2.2096365819325294,  None, None, 0.1)
        self.assertAlmostEqual(self.line.end().x, -2.895220058353975,  None, None, 0.1)
        self.assertAlmostEqual(self.line.end().y, -4.076481425654336,  None, None, 0.1)


class circleTests(unittest.TestCase):
    def setUp(self):
        point1 = PointT(1, 2)
        point2 = PointT(4, 3)

        self.circle1 = CircleT(point1, 3)
        self.circle2 = CircleT(point2, 2)

    def tearDown(self):
        self.circle1 = None
        self.circle2 = None

    def testcen(self):
        self.assertTrue(self.circle1.cen().x == 1)
        self.assertTrue(self.circle1.cen().y == 2)

    def testrad(self):
        self.assertTrue(self.circle1.rad() == 3)

    def testarea(self):
        self.assertAlmostEqual(self.circle1.area(), 28.274333882308138,  None, None, 0.1)

    def testintersect(self):
        self.assertTrue(self.circle1.intersect(self.circle2) == True)

    def testconnection(self):
        (self.circle1).connection(self.circle2)
        
        self.assertAlmostEqual((self.circle1).connection(self.circle2).beg().x, 1,  None, None, 0.1)
        
        self.assertAlmostEqual((self.circle1).connection(self.circle2).end().y, 3,  None, None, 0.1)

    def testforce(self):
        self.assertAlmostEqual(self.circle1.force((self.circle1.counter(self.circle2))), 2.3706000203064544e-09,  None, None, 0.1)
        

class dequeTests(unittest.TestCase):
    def setUp(self):
        point1 = PointT(1, 2)
        point2 = PointT(3, 4)
        point3 = PointT(10, 7)
        point4 = PointT(8, 2)
        

        self.circle1 = CircleT(point1, 1)
        self.circle2 = CircleT(point2, 2)
        self.circle3 = CircleT(point3, 1)
        self.circle4 = CircleT(point4, 1)

        Deque.Deq_pushBack(self.circle1)
        Deque.Deq_pushBack(self.circle2)
        Deque.Deq_pushBack(self.circle3)
        Deque.Deq_pushBack(self.circle4)

    def tearDown(self):
        circle1 = None
        circle2 = None

    def testDeq_back(self):
        

        self.assertTrue(Deque.Deq_back().rad() == 1)

    def testDeq_front(self):
        

        self.assertTrue(Deque.Deq_back().rad() == 1)
        
   
    def testDeq_disjoint(self):
        
        self.assertTrue(Deque.Deq_disjoint() == True)

    def testDeq_totalArea(self):
        
        self.assertAlmostEqual(Deque.Deq_totalArea(), 109.9557428756428,  None, None, 0.1)

    def testDeq_averageRadius(self):
        
        self.assertAlmostEqual(Deque.Deq_averageRadius(), 1.0,  None, None, 0.1)
    
        

if __name__ == '__main__':
    unittest.main()
