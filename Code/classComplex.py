# -*- coding: utf-8 -*-
"""
# Implementation of ADT Complex

We now implement the ADT Complex. 

We use the well-known operators +, -, * and abs. We can overwrite these operators. You can find the names of their corresponding functions at this link
https://docs.python.org/3/library/operator.html


- operator.__add__(a, b) is equivalent to a + b,
- operator.__sub__(a, b) is equivalent to a - b,
- operator.__mul__(a, b) is equivalent to a * b,
- operator.__abs__(a) is equivalent to abs(a),
- operator.__neg__(a) is equivalent to -a,

Anyway, you can also define your own methods (with different names to implement these functions).
"""

import math 

class Complex:

    def __init__(self, a=0,b=0):
      """This is the constructor method. By default, the values for the attributes are 0"""
      self.a = a #real part
      self.b = b #imaginary part

    def __str__(self):
      """Returns a string representing the complex number"""
      if self.a==0 and self.b==0:
        return '0'
      
      if self.a==0:
        text='{}i'.format(self.b)
      elif self.b==0:
        text='{}'.format(self.a)
      elif self.b<0:
        text='{}{}i'.format(self.a,self.b)
      elif self.b>0:
        text='{}+{}i'.format(self.a,self.b)
        
      return text


    def __neg__(self):
      """Returns the negation of the complex number"""
      negComplex=Complex(-self.a,-self.b)
      return negComplex
    
    def __add__(self,other):
      """Returns a nex complex number, which is the sum of the invoking complex number
      and the other parameter"""
      sumComplex=Complex(self.a+other.a, self.b + other.b)
      return sumComplex
    
    def __sub__(self,other):
      
      return Complex(self.a-other.a, self.b - other.b)
    
    def __mul__(self,other):
      """Returns a new complex number, which is the multiplication of the invoking complex number
      and the other parameter"""
      multComplex=Complex(self.a*other.a-self.b*other.b,self.a*other.b+self.b*other.a)
      return multComplex
    
    def __abs__(self):
      """Returns the module of the invoking complex number"""
      return math.sqrt(math.pow(self.a,2)+math.pow(self.b,2))
      

#Now, we test the different methods    

c=Complex(3,5)
print('c={}'.format(str(c)))

print('-{} = {}'.format(str(c),str(-c)))
print()


other=Complex(2,1)
print('other={}'.format(str(other)))
print('({})+({}) = {}'.format(str(c),str(other),str(c+other)))
print('({})-({}) = {}'.format(str(c),str(other),str(c-other)))
print('({})*({}) = {}'.format(str(c),str(other),str(c*other)))

print()
print('abs({}) = {}'.format(str(c),str(abs(c))))