# -*- coding: utf-8 -*-
"""
# Doubly Linked List (+ removeAll method)

In this subclass, we extend the doubly linked list class by adding the removeAll method.
This method takes an element as parameter and removes all its occurrences from the list.
The subclass includes two different verions for the method:
1.   by traversing node by node and updating the references.
2.   by using other methods such as count or removeAt.
"""
from doublylinkedlist import DoublyLinkedList


class DListWithRemoveAll(DoublyLinkedList):
  """This subclass is an extension of the DoublyLinkedList. In this subclass,
  we add two different methods for the removeALL method"""
  
  def removeAll(self,e):
    """This functions takes an element as parameter and removes all its 
    occurrences from the list"""
    pos=self.contains(e)
    while pos!=-1:
      self.removeAt(pos)
      pos=self.contains(e)
      
  def removeAll2(self,e):
    """This functions takes an element as parameter and removes all its 
    occurrences from the list"""
    node=self.head
    while node:
        if node.element==e:
            #we must remove this node
            if node is self.head:
                self.removeFirst()
            elif node is self.tail:
                self.removeLast()
            else:
                prevNode=node.prev
                nextNode=node.next
                prevNode.next=nextNode
                nextNode.prev=prevNode
                self.size-=1
        node=node.next

      
#main      
 
import random 

def test():
    """This method helps us to assess the above methods"""
    
    l=DListWithRemoveAll()
    for i in range(10):
        #l.addLast(i)
      #we add a random number N, such as 0<=N<=10      
      l.addLast(random.randint(0,5))
      
    
    print("original list: ", str(l))
    l.removeAll(0)
    print("after removing 0: ", str(l))
    l.removeAll(1)
    print("after removing 1: ", str(l))
    l.removeAll(2)
    print("after removing 2: ", str(l))
    l.removeAll(3)
    print("after removing 3: ", str(l))
    l.removeAll(6)
    print("after removing 6 (which does not exist!!): ", str(l))

def test2():
    """This method helps us to assess the above methods"""
    
    l=DListWithRemoveAll()
    for i in range(10):
        #l.addLast(i)
      #we add a random number N, such as 0<=N<=10      
      l.addLast(random.randint(0,5))
      
    
    print("original list: ", str(l))
    l.removeAll2(0)
    print("after removing 0: ", str(l))
    l.removeAll2(1)
    print("after removing 1: ", str(l))
    l.removeAll2(2)
    print("after removing 2: ", str(l))
    l.removeAll2(3)
    print("after removing 3: ", str(l))
    l.removeAll2(6)
    print("after removing 6 (which does not exist!!): ", str(l))
    
test()
test2()
