# -*- coding: utf-8 -*-
"""
MyPolynomialADT

"""

class Polynomial:
  """Python class to represent polynomial functions"""
  
  def __init__(self, coefficients):
    """This constructor takes the coefficients for the terms of the polynomial.
    We assume that the constant term (degree 0) is stored at the index 0 in the list, 
    the term with degree 1 is at the index 1, and so on..."""
    self.coefficients = coefficients
    
  def __str__(self):
    "It retuns a string representing the polynomial function"
    constant=self.getCoefficient(0)
    result=''
    if constant!=0:
      result=str(constant)
    
    for i in range(1,self.degree()+1):
      term=self.getCoefficient(i)
      if term!=0:
        if result!='' and term>0:
          result=result+str('+')
        if term==1:
          term=''
        elif term==-1:
          term='-'
        result  = result + str(term)+str('x')
        
        if i>1:
          result=result+str('^')+str(i)
    
    
    return result
  
  def degree(self):
    """It returns the degree of the polynomial"""
    return len(self.coefficients)-1

  def getCoefficient(self,i):
    """It returns the coefficient of the term with degree i"""
    if i<0 or i>self.degree():
      print('{} index out of range'.format(i))
      return None
    
    #if i not in range(0,self.degree()+1):
    #  print('{} index out of range'.format(i))
    #  return None
    
    return self.coefficients[i]

  
  def setCoefficient(self,i,newValue):
    """It modifies the coefficient of the term with degree i to newValue"""
    
    
    if i not in range(0,self.degree()+1):
      print('{} index out of range'.format(i))
      return 
    
    self.coefficients[i]=newValue


  def evaluate(self,x):
    "This method returns the value of the polynomial functions for x"
    result=0
    for i in range(0,self.degree()+1):
      result += self.getCoefficient(i)*pow(x,i)
    
    return result
  
 
  
  def __add__(self,q):
    """It returns a new polynomial which is the sum of the invoking polynomial (self)
    and q. """
    
    #Create a new polynomial that is a copy of the polynomial with greater degree
    if (self.degree()>=q.degree()):
      sumPol=Polynomial(self.coefficients)
      #now, we have to add the coefficients from q
      for i in range(0,q.degree()+1):
        sumPol.setCoefficient(i, sumPol.getCoefficient(i)+q.getCoefficient(i))
    else:
      sumPol=Polynomial(q.coefficients)
      #now, we have to add the coefficients from self
      for i in range(0,self.degree()+1):
        sumPol.setCoefficient(i, sumPol.getCoefficient(i)+self.getCoefficient(i))
          
        
    return sumPol
        
  


"""Now, we include some instructions for testing the different methods"""

#we create a polynomial
p=Polynomial([1,2,3,0,0,-2,8])

#we test the method toString 
print('p={}'.format(str(p)))

#we test the method degree 
print('Degree:{}'.format(p.degree()))

#we test the method getCoefficient for different indexes
print('getCoefficient(0)={}'.format(p.getCoefficient(0)))
print('getCoefficient(1)={}'.format(p.getCoefficient(1)))
print('getCoefficient(2)={}'.format(p.getCoefficient(2)))
print('getCoefficient(3)={}'.format(p.getCoefficient(3)))


#we test the method setCoefficient for several values
p.setCoefficient(0,0)
print('setCoefficient(0,0)={}'.format(str(p)))

p.setCoefficient(0,5)
print('setCoefficient(0,5)={}'.format(str(p)))

p.setCoefficient(1,-1)
print('setCoefficient(1,-1)={}'.format(str(p)))

p.setCoefficient(2,1)
print('setCoefficient(2,1)={}'.format(str(p)))

p.setCoefficient(3,4)
print('setCoefficient(3,4)={}'.format(str(p)))

#we test the method evaluate for several values
print('evaluate(0)={}'.format(p.evaluate(0)))
print('evaluate(1)={}'.format(p.evaluate(1)))
print('evaluate(2)={}'.format(p.evaluate(2)))


q=Polynomial([3,-3,7,2,0,1])
print('q={}'.format(str(q)))
print('p+q={}'.format(str(p+q)))