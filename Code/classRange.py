# -*- coding: utf-8 -*-

class Range:
  """A class that mimics the built-in range class."""

  def __init__(self, start, end, step=1):
    """Initialize a Range instance
      - start is the initial value of the range,
      - end is the upper limit. This value does not belong
      to the range.
      - step: by default 1.
      """
    if step==0:
      raise ValueError('step cannot be 0') #we throw an error
    self.start=start
    self.end=end
    self.step=step
   
  def __len__(self):
    """returns the number of elements in the range"""
    result=(self.end-self.start+self.step-1)//self.step
    return max(0,result)
  
  def __getitem__(self,i):
    """Returns the ith element of the sequence"""
    if i<0 or i>len(self):
      raise IndexError('index out of range')
    
    return self.start + i*self.step
  
  def __str__(self):
    """Returns a string containing the sequence"""
    result='['
    for i in range(0,len(self)):
      result  = result + str(self[i]) + ','
    result=result[:-1]
    result+=']'
    return result
  
  def __sum__(self):
    """Returns a string containing the sequence"""
    elem=self.start
    result=0
    while elem<self.end:
      result+=elem
      elem=elem+self.step
      
    
    return result
  
r=Range(2,20,2)
print(str(r))
print("size = {}".format(len(r)))
print("sum = {}".format(sum(r)))