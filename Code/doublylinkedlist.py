# -*- coding: utf-8 -*-
"""
# Doubly Linked List

First, we must implement the class Node to store the nodes. In addition to the element and the reference to the next node, the class includes a reference, **prev**, to the previous node.
"""

class DoublyNode:
  def __init__(self, e, n=None, p=None ):
    self.element = e
    self.next = n
    self.prev = p

class DoublyLinkedList:
  def __init__(self):
    """creates an empty list"""
    self.head=None
    self.tail=None
    self.size=0
    
  def isEmpty(self):
    """Checks if the list is empty"""
    return self.head is None   
  
  def addFirst(self,e):
    """Add a new element, e, at the beginning of the list"""
    #create the new node
    newNode=DoublyNode(e)
    #the new node must point to the current head
    
    if self.isEmpty():
      self.tail=newNode
    else:
      newNode.next=self.head
      self.head.prev=newNode
      
    #update the reference of head to point the new node
    self.head=newNode
    #increase the size of the list  
    self.size=self.size+1
    
    
  def addLast(self,e):
    """Add a new element, e, at the end of the list"""
    #create the new node
    newNode=DoublyNode(e)
    
    if self.isEmpty():
      self.head=newNode
    else:
      newNode.prev=self.tail
      self.tail.next=newNode
      
    #update the reference of head to point the new node
    self.tail=newNode
    #increase the size of the list  
    self.size=self.size+1
   
  
  def __str__(self):
    """Returns a string with the elements of the list"""
    temp=self.head
    strList=''
    while temp is not None:
      strList=strList+','+str(temp.element)
      temp=temp.next
    return strList[1:]
  
  def removeFirst(self):
    """Returns and remove the first element of the list"""
    if self.isEmpty():
      print("Error: list is empty")
      return None
    
    result=self.head.element 
    self.head= self.head.next 
    if self.head is None:
      self.tail=None
    else:
      self.head.prev = None

    self.size=self.size-1
    return result
  
  def removeLast(self):
    """Returns and remove the last element of the list"""
    if self.isEmpty():
      print("Error: list is empty")
      return None
    
    result=self.tail.element 
    self.tail= self.tail.prev 
    if self.tail is None:
      self.head=None
    else:
      self.tail.next = None

    self.size=self.size-1
    return result
  
  
  def insertAt(self,index,e):
    """It inserts the element e at the index position of the list"""
    if index<0 or index>self.size:
      print('Error: index out of range')
      return
    
    if index==0:
      self.addFirst(e)
    elif index==self.size: 
	    self.addLast(e)
    else:
      i=0
      aux=self.head
      while i<index:
        aux=aux.next
        i=i+1
      #aux is the node at the index position
      previous=aux.prev
      newNode=DoublyNode(e)
      newNode.next=aux
      newNode.prev=previous
      aux.prev=newNode
      previous.next=newNode
      self.size= self.size+1
      
      
  def getAt(self,index):
    """Returns the element at the index position in the list"""
    
    #first, check the index is a right position in the list
    if index<0 or index>=self.size:
      print(index,'error: index out of range')
      return None
      
    #we need to reach the node at the index position in the list
    i=0
    current=self.head
    while  i<index:
      current=current.next
      i+=1
    #here, current is the node at the index position in the list
    #we return its element
    return current.element
      
      
  def contains(self,e):
    """It returns the first position of e into the list. If the element 
    does no exist, then it returns -1"""
    
    index=-1
    
    found=False
    
    current=self.head
    #we traverse the nodes while found is not True. 
    while current is not None and found==False:
      if current.element==e:
        found=True   #the loop condition becomes False
      current=current.next
      index=index+1
    
    #Warning: if e does not exist,  
    #index is the number of nodes in the list    
    if found:
      return index
    else:
      return -1
    
  def removeAt(self,index):
    """This methods removes the node at the index position in the list"""
    
    #We must check that index is a right position in the list
    #Remember that the indexes in a list can range from 0 to size-1
    if index<0 or index>=self.size:
      print(index,'Error: index out of range')
      return 
       
    if index==0:
      self.removeFirst()
    elif index==self.size-1:
      self.removeLast()
    else:
      #we must to reach the node at the index position
      i=0
      node=self.head
      while i<index:
        node=node.next
        i=i+1
      
      prevNode=node.prev
      nextNode=node.next
      
      prevNode.next=nextNode
      nextNode.prev=prevNode
      self.size=self.size-1

  def show(self,opc):
    result=''
    if opc==0:
      node=self.head
      while node:
        result += str(node.element)+ ' '
        node=node.next
    else:
      node=self.tail
      while node:
        result += str(node.element)+ ' '
        node=node.prev
    print(result[:-1])

#main
    
def test():
    """This functions helps us to assess each method of the class"""
    l=DoublyLinkedList()
    
    for i in range(10):
      l.addLast(i)
      
    l.show(0)
    l.show(1)
    print(str(l))
    
    l.removeAt(5)
    print('after removing at 5:', str(l))
    l.removeAt(0)
    print('after removing at 0:', str(l))
    l.removeAt(l.size-1)
    print('after removing at size-1:', str(l))
    
    l.insertAt(0,0)
    print('after inserting at 0, 0:', str(l))
    l.insertAt(l.size,9)
    print('after inserting at size, 9:', str(l))
    l.insertAt(5,1)
    print('after inserting at 5, 1:', str(l))
    l.insertAt(5,1)
    print('after inserting at 5, 1:', str(l))
    
    result=''
    for i in range(l.size):
      result += ' ' + str(l.getAt(i))
    
    print(result[1:])
    
    print('contains 10',l.contains(10))
    print('contains 4',l.contains(4))
    print('contains 1',l.contains(1))
    
    l.removeLast()
    print('after removing last',str(l))
    l.removeFirst()
    print('after removing first',str(l))
    while not l.isEmpty():
      print("removing",l.removeLast())
   
test()