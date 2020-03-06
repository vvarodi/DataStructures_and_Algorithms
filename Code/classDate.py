# -*- coding: utf-8 -*-
"""
  Implementation of our Date class
"""

#This is an atribute of the class. That is, all objects share this attribute.
MONTH={1:'January',2:'February',3:'March',4:'April',5:'May',
      6:'June', 7:'July', 8:'August', 9:'September',
      10:'October',11:'November',12:'December'}

class Date:
   
  def __init__(self, day, month, year):
    self.day = day
    self.month = month
    self.year = year


  def day(self):
    return self.day
    
  def month(self):
    return self.month
    
  def year(self):
    return self.year
      
  def monthName(self):
    return MONTH[self.month] 
    
  def __str__(self):
    return str(self.day)+'-'+str(self.month)+'-'+str(self.year)
    
  def is_leap_year(self):
    """Determine whether a year is a leap year."""
    return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)

    """Now, we implement some operators to compare dates.
    
    - operator.__lt__(a, b) is equivalent to a < b,
    - operator.__le__(a, b) is equivalent to a <= b,
    - operator.__eq__(a, b) is is equivalent to a == b,
    - operator.__ne__(a, b) is equivalent to a != b
    - operator.__ge__(a, b) is equivalent to a >= b
    - operator.__gt__(a, b) is equivalent to a > b
    
    
    You can find more information about these operators at :
    https://docs.python.org/3/library/operator.html
    """
  def __eq__(self,other):
    """#operator.__eq__(a, b) is is equivalent to a == b"""
    return self.day==other.day and self.month==other.month and self.year==other.year

  def __ne__(self,other):
    """#operator.__ne__(a, b) is equivalent to a != b"""
    return self.day!=other.day or self.month!=other.month and self.year!=other.year

  def __lt__(self,other):
    """#operator.__lt__(a, b) is equivalent to a < b,"""
    if self.year < other.year:
      return True
    elif self.year > other.year:
      return False

    ## self.year == other.year
    if self.month < other.month:
      return True
    elif self.month > other.month:
      return False

    #self.month = other.month
    if self.day<other.day:
      return True
    else:
      return False


"""Now, we create some instances (objects) of the Date class, and test some methods."""

d1=Date(31,1,2019)
print("Date: {} ".format(str(d1)))
print("Its month name is {}".format(d1.monthName()))
print("Is it a leap year? {}".format(d1.is_leap_year()))
print()

d2=Date(3,10,2016)
print("Date: {} ".format(str(d2)))
print("Its month name is {}".format(d2.monthName()))
print("Is it a leap year? {}".format(d2.is_leap_year()))

print('{} == {} ? {}'.format(d1,d2,d1==d2))
print('{} == {} ? {}'.format(d1,d1,d1==d1))

print('{} != {} ? {}'.format(d1,d2,d1!=d2))

print('{} < {} ? {}'.format(d1,d2,d1<d2))
print('{} < {} ? {}'.format(d2,d1,d2<d1))
print('{} < {} ? {}'.format(d1,d1,d1<d1))
