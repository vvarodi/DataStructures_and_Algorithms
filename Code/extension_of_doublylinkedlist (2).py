# -*- coding: utf-8 -*-


from doublylinkedlist import DoublyLinkedList
from doublylinkedlist import DoublyNode

class DoublyLinkedListExt1(DoublyLinkedList):
  """This class is a subclass of DoublyLinkedList. In this subclass,
  we add new methods such as getAtRev, getAtEff, insertAtEff and removeAtEff"""

  def getAtRev(self,index):
    """Returns the element at index position of the list, starting from the end"""
    aux=self.tail
    i=0
    while aux!=None:
      if i==index:
        return aux.element
      aux=aux.prev
      i+=1
    
    print(index,' is out of range')
    return None
  
  def getAtEff(self, index):
    """Returns the element at the index position taking advantage of the
    reversing order"""
    if index<0 or index>=self.size:
      print('error: index out of range')
    if index <= self.size//2:
      print(index,'searching from the beginning')
      return self.getAt(index)
    else:
      print(index,'searching from the tail')

      aux=self.tail
      i=self.size-1
      while aux!=None:
        if i==index:
          return aux.element
        aux=aux.prev
        i-=1
        

  def insertAtEff(self,index,elem):
    """It inserts the element e at the index position of the list, 
    taking advantage of traversing the list backward"""
    if index<0 or index>self.size:
      print('Error: index out of range')
      return
    
    if index==0:
      self.addFirst(elem)
    elif index==self.size:
      self.addLast(elem)
    elif index<=self.size//2:
      print(index,'insert- starting from the head')
      self.insertAt(index,elem)
    else:
      print(index,'insert- starting from the end')
      i=self.size-1
      aux=self.tail
      while i>index:
        aux=aux.prev
        i-=1
      #aux is the node at the index position
      previous=aux.prev
      newNode=DoublyNode(elem)
      newNode.next=aux
      newNode.prev=previous
      aux.prev=newNode
      previous.next=newNode
      self.size= self.size+1
      
  def removeAtEff(self,index):
    """It removes the element at the index position of the list, 
    taking advantage of traversing the list backward"""
    if index<0 or index>self.size:
      print('Error: index out of range')
      return
    
    if index==0:
      return self.removeFirst()
    elif index==self.size-1:
      return self.removeLast()
    elif index<=self.size//2:
      print(index,'remove- starting from the head')
      return self.removeAt(index)
    else:
      #we must to reach the node at the index position
      print(index,'remove- starting from the tail...')
      i=self.size-1
      node=self.tail
      while i>index:
        node=node.prev
        i-=1
      
      #node is the node that we want to remove
      node.prev.next=node.next
      node.next.prev=node.prev
      
      self.size=self.size-1
      return node.element
  
    
    
#main    
def test():
    l=DoublyLinkedListExt1()
    
    for i in range(10):
      l.addLast(i)
      
    print(str(l))
    
    print("l.getAtRev(0)",l.getAtRev(0))
    
    print("l.getAtRev(1)",l.getAtRev(1))
    print("l.getAtRev(8)",l.getAtRev(8))
    print("l.getAtRev(10)",l.getAtRev(10))
    
    
    
    #for i in range(l.size):
    #  print(l.getAtEff(i))
      
    
    
    l.removeAtEff(1)
    print("after l.removeAtEff(1)",str(l))
    
    l.removeAtEff(8)
    print("after l.removeAtEff(8)",str(l))
    
    l.removeAtEff(-1)
    print("after l.removeAtEff(-1)",str(l))
    
    
    l.insertAtEff(l.size-1,5)
    print("after l.insertAtEff(l.size-1,5)",str(l))
    l.insertAtEff(l.size-3,5)
    print("after l.insertAtEff(l.size-3,5)",str(l))
    l.insertAtEff(3,5)
    print("after l.insertAtEff(3,5)",str(l))
    

test()