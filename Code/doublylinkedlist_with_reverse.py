# -*- coding: utf-8 -*-
"""
1.   a method that reverse the elements by swapping them.
2.   a method that reverse the elements by swapping the references of the nodes.
"""
from doublylinkedlist import DoublyLinkedList


class DListWithReverse(DoublyLinkedList):
  """This subclass is an extension of the DoublyLinkedList. In this subclass,
  we add two different methods for reversing the list"""
  
  def reverse(self):
    """This functions reverse the list by swapping its elements"""
    if self.isEmpty():
      print('The list is empty')
      return
    
    left=self.head
    rigth=self.tail
    i=0
    while i<=self.size//2:
      #swap the elements
      temp=left.element
      left.element=rigth.element
      rigth.element=temp
      #advance
      i+=1
      left=left.next
      rigth=rigth.prev
      
      
  def reverse2(self):
    """This functions reverse the list by swapping its references"""
   
    
    preNode=None
    node = self.head
    
    #swap next and prev references for all nodes of the list
    while node is not None:
      preNode=node.prev
      node.prev=node.next
      node.next=preNode
      #we must advance to the next node (which now is the prev node)
      node=node.prev
      
    #finally, we must also swap head and tail  
    temp=self.head
    self.head=self.tail
    self.tail=temp

import random 

def test():
    """This method helps us to assess the above methods"""
    
    l=DListWithReverse()
    for i in range(10):
        #l.addLast(i)
      #we add a random number N, such as 0<=N<=10      
      l.addLast(random.randint(0,10))
      
    
    print("original list: ", l.toString())
    l.reverse2()
    print("reverse list by swapping the references",l.toString())
    l.reverse()
    print("reverse list by swapping the elements",l.toString())

    
test()
