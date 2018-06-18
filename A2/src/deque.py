## @file deque.py
#  @title deque
#  @author Polly Yao
#  @date 2/19/2017

## @brief This class represents a queue




import circleADT
import pointADT
import lineADT
import math

class Deque:
    
  MAX_SIZE = 20
  
  d = []

## @brief Constructor for the queue
  @staticmethod
  def Deq_init():
    Deque.d = []

## @brief This function push circles onto the back of the queue
#  @param c takes in circle
  @staticmethod
  def Deq_pushBack(c):
    d = Deque.d
    size = len(d)
    if size == Deque.MAX_SIZE:
      raise Full("Maximum size exceeded")
    
    d.append(c)
    

    Deque.d = d


## @brief This function push circles onto the front of the queue
#  @param c takes in circle
  @staticmethod
  def Deq_pushFront(c):
    d = Deque.d
    size = len(d)
    if size == Deque.MAX_SIZE:
      raise Full("Maximum size exceeded")
    
    d.insert(0, c)
   

    Deque.d = d


## @brief This function remove circles from the back of the queue

  @staticmethod
  def Deq_popBack():
    d = Deque.d
    size = len(d)
    if size == 0:
      raise Empty("Queue is empty")
    
    d.pop()
   

    Deque.d = d

## @brief This function remove circles from the front of the queue
  @staticmethod
  def Deq_popFront():
    d = Deque.d
    size = len(d)
    if size == 0:
      raise Empty("Queue is empty")
    
    d.pop(0)
  

    Deque.d = d


## @brief This function returns the last circle in the queue
#  @return the last circle in the queue
  @staticmethod
  def Deq_back():
      size = len(Deque.d)
      if size == 0:
          raise Empty("Queue is empty")
      
      
      return Deque.d[size-1]

## @brief This function returns the first circle in the queue
#  @return the first circle in the queue
  @staticmethod
  def Deq_front():
      size = len(Deque.d)
      if size == 0:
          raise Empty("Queue is empty")
      
      
      return Deque.d[0]

## @brief This function measure the length the queue
#  @return the the length of the queue
  @staticmethod
  def Deq_size():
      size = len(Deque.d)
      return size


## @brief This function if there are any circles intersect each other in the queue
#  @return True if there is at least one circle intersect with another, return False otherwise
  @staticmethod
  def Deq_disjoint():
      size = len(Deque.d)

      if size == 0:
          raise Empty("Queue is empty")
      array = []
      for i in range(len(Deque.d)):
          for j in range(i+1, len(Deque.d)):
             distance = math.sqrt((Deque.d[i].cen().y - Deque.d[j].cen().y)**2 + (Deque.d[i].cen().x - Deque.d[j].cen().x)**2)
             radii = Deque.d[i].rad() + Deque.d[j].rad()

             if (radii >= distance):
                 array.append(True)
             else:
                 array.append(False)

      cou = array.count(True)
      if cou > 0:
          return True
      else:
          return False
 


## @brief This function compute the area for each of the circle in the queue, and add all the area together
#  @return total area
  @staticmethod
  def Deq_totalArea():
      size = len(Deque.d)

      if size == 0:
          raise Empty("Queue is empty")
      
      array = []
      
      for element in range(len(Deque.d)):
          area = (math.pi)*((Deque.d[element].rad())**2)
          array.append(area)
          
      a = sum(array)    
      return a




## @brief This function compute the average radius of the circles in the queue
#  @return avaerage radius
  @staticmethod
  def Deq_averageRadius():
      size = len(Deque.d)

      if size == 0:
          raise Empty("Queue is empty")
      array = []
      
      for element in range(len(Deque.d)):
          
          array.append(Deque.d[element].rad())
          
      a = sum(array)
      
      b = len(array)
      
      average = float(a/b)
      return average

    
          


    
