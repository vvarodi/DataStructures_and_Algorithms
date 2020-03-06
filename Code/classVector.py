
# -*- coding: utf-8 -*-
"""

#def dot_product2(self, v2):
#    
#    #return sum(map(operator.mul, v1, v2))
#    for x in self:
#        
#
#def vector_cos5(v1, v2):
#    prod = dot_product2(v1, v2)
#    len1 = math.sqrt(dot_product2(v1, v1))
#    len2 = math.sqrt(dot_product2(v2, v2))
#    return prod / (len1 * len2)

import math

class Vector:
  
  def __init__(self,dim):
    """Creates a vector of dimension dim. 
    All its coordinates are 0's"""
    self.items=[0]*dim
    
    
    
  def __len__(self):
    """Returns the dimension of the vector."""  
    return len(self.items)  
  
  def __getitem__(self,i):
    """Returns the ith coordinate of the vector"""
    return self.items[i]
    
  def __setitem__(self,i,newValue):
    """Sets the ith coordinate to the given value"""
    if i<0 or i>=len(self):
      print('Error: index out of range')
      return
    
    self.items[i]=newValue
    
  
  def __str__(self):
    """Returns a string containing the vector"""
    result='('
    for i in range(0,len(self)):
      result  = result + str(self[i]) + ','
    result=result[:-1]
    result+=')'
    return result
  
  
  
  def __add__(self,other):
    """Returns a new vector, which is the sum of the invoking vector and the param other"""
    
    if len(self)!=len(other):
      print('Error: vectors with different dimensions')
      return None
    
    #creates a new vector
    sumV=Vector(dim)
    for i in range(0,len(self)):
      sumV[i]=self[i]+other[i]  
      
    return sumV
    
  def __eq__(self,other):
    """checks if the two vectors have the same coordinates"""
    if len(self)!=len(other):
      return False
    
    for i in range(0,len(self)):
      if self[i] != other[i]:
        return False
      
    return True

  def dot(self,other):
    if len(self)==len(other) and len(self)!=0:
        return sum([self[n]*other[n] for n in range(len(self))])
    else:
        return 0        

  def cosinedis(self, other):
    prod = self.dot(other)
    len1 = math.sqrt(self.dot(self))
    len2 = math.sqrt(other.dot(other))
    return prod / (len1 * len2)

"""Now, let me create some vectors and try the different methods, which we have already implemented."""

import random
dim=4
v1=Vector(dim)
v2=Vector(dim)
v3=Vector(dim)

#This loop allows us to initialize the coordinates of the two vectors
#in a random way, with values from 0 to 99 
for i in range(0,dim):
  v1[i]=random.randint(0,100)
  v2[i]=random.randint(0,100)
  v3[i]=v1[i]

#we show the three vectors vectors  
print("v1={}".format(str(v1)))  
print("v2={}".format(str(v2)))  
print("v3={}".format(str(v3)))  


#we check if they are equal
print("{}=={}?={}".format(v1,v3,v1==v3))
print("{}=={}?={}".format(v1,v2,v1==v2))

#we sum the two vectors
print("{}+{}={}".format(v1,v2,v1+v2))


#we calculate the scalar product of two vectors
print("dot({},{})={}".format(v1,v2,v1.dot(v2)))


#we calculate the cosine distance of two vectors
print("cosinedis({},{})={}".format(v1,v2,v1.cosinedis(v2)))
print("cosinedis({},{})={}".format(v1,v3,v1.cosinedis(v3)))

print("cosinedis({},{})={}".format(v1,v1,v1.cosinedis(v1)))