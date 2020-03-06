# -*- coding: utf-8 -*-
"""
# Printer
"""

class Queue:
  """FIFO Queue implementation using a Python list as storage. 
  We add new elements at the tail of the list (enqueue)
  and remove elements from the head of the list (dequeue)."""
  
  def __init__(self):
    """Create an empty queue"""
    self.items=[]
    
  def enqueue(self,e):
    """Add the element e to the tail of the queue"""
    self.items.append(e)
    
  def dequeue(self):
    """Remove and return the first element in the queue"""
    if self.isEmpty():
      print('Error: Queue is empty')
      return None
    #remove first item from the list
    return self.items.pop(0) 
  
  def front(self):
    """Return the first element in the queue"""
    if self.isEmpty():
      print('Error: Queue is empty')
      return None
    
    #returns first element in the list
    return self.items[0] 
  
  def __len__(self):
    """Return the number of elements in the queue"""
    return len(self.items)
  
  def isEmpty(self):
    """Return True if the queue is empty"""
    return len(self.items)==0
  
  

class Request:
  """This class represent a request to be printed"""
  def __init__(self,idMachine,nameFile):
    self.idMachine=idMachine
    self.nameFile=nameFile
    
  def __str__(self):
    return self.idMachine+"\t"+self.nameFile

class Printer:
  """This class simulates a network printer"""
  def __init__(self):
    self.q=Queue()
    
  def addRequest(self, request):
    self.q.enqueue(request)
  
  def getNumRequest(self):
    return len(self.q)
  
  def showAll(self):
    for r in self.q.items:
      print(str(r))
  
  def printWork(self):
    if self.q.isEmpty():
      print('There is no work to print')
      return 
    
    r=self.q.dequeue()
    print("printing...",str(r))
    
  def printAll(self):
    while not self.q.isEmpty():
      self.printWork()
  
  
##main 
p=Printer()
p.addRequest(Request("293939","Unit2.pdf"))
p.addRequest(Request("111","Unit1.pdf"))
p.addRequest(Request("333","Unit3.pdf"))
p.showAll()
print('Num works', p.getNumRequest())

print()
print('print the first work')
p.printWork()
print('showing all')
p.showAll()
print('printing all')
p.printAll()

print('Num works', p.getNumRequest())

