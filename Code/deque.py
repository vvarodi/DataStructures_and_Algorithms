# -*- coding: utf-8 -*-
"""
# Deques 

Unlike stack and queue, the deque (pronounced 'deck') has very few restrictions. 

A **deque**, also known as a **double-ended queue**, is a  collection of items similar to the queue. It has two ends, a front and a tail.

New items can be added at either the front or the tail. 
Likewise, existing items can be removed from either end. 

In a sense, this hybrid linear structure provides all the capabilities of stacks and queues in a single data structure. 

## The Deque Abstract Data Type

The **deque** abstract data type is defined by the following structure and operations. 

A deque is a collection of items where items are added and
removed from either end, either front or tail. The deque operations are given below: 

- Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.

- addFirst(item) adds a new item to the front of the deque. It returns nothing.

- addLast(item): adds a new item to the tail of the deque. It returns
nothing.

- removeFirst(): removes the front item from the deque. The deque is modified. It returns the item. 

- removeLast(): removes the tail item from the deque. It returns the item. The deque is modified.

- isEmpty(): returns True if the deque is empty, False otherwise.

- size(): returns the number of items in the deque. 

## Implementing a Deque using Python list

Our implementation assumes that the front of the deque is at position 0 in the list
"""

class Deque:
  
  def __init__(self):
    """Create an empty deque"""
    self.items=[]
    
  def addFirst(self,e):
    """Add at the beginning of the deque"""
    self.items.insert(0,e)
    
  def addLast(self,e):
    """Add at the tail of the deque"""
    self.items.append(e)
    
  def removeFirst(self):
    """Remove and return the first element in the deque"""
    if self.isEmpty():
      print('Error: Deque is empty')
      return None
    #remove first item from the list
    return self.items.pop(0) 
  
  def removeLast(self):
    """Remove and return the element at the tail of the deque"""
    if self.isEmpty():
      print('Error: Deque is empty')
      return None
    #remove last item from the list
    return self.items.pop() 
  
  def size(self):
    """Return the number of elements in the deque"""
    return len(self.items)
  
  def isEmpty(self):
    """Return True if the deque is empty"""
    return len(self.items)==0
  
  def toString(self):
    strQ=''
    for x in self.items:
      strQ=strQ+','+str(x)
    #print the elements of the list
    return strQ[1:]
  
  
q=Deque()
print('isEmpty()',q.isEmpty())
q.addLast(4)
q.addLast(5)
q.addFirst(3)
q.addFirst(2)
q.addFirst(1)
print('Content of queue',q.toString())
print('isEmpty()',q.isEmpty())
print('removeFirst():',q.removeFirst())
print('removeLast():',q.removeLast())
print('Content of deque',q.toString())
print('size:',q.size())