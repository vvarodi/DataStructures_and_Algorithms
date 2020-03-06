# -*- coding: utf-8 -*-
"""
First, we must implement the Node class, which has two attributes: element and next, which points to the following node of the list.
"""

class Node:
  def __init__(self, e):
    self.element = e
    self.next = None

"""Now, we can implement the class for a singly linked list. Our class only uses a refererence, head, for storing the first node, respectively. Moreover, it includes an atributte, named size, which stores the number of elements in the list."""

class SinglyLinkedList2:
  """This is the implementation of a singly linked list. We use 
  a reference to the first node, named head, and also a reference 
  to the last node, named as tail. Also we keep an attribute, size, 
  to store the number of nodes"""
  def __init__(self):
    self.head=None
    self.tail=None
    self.size=0
    
    
  def isEmpty(self):
    """Checks if the list is empty"""
    return self.head is None   
    

  def addFirst(self,e):
    """Add a new element, e, at the beginning of the list"""
    #create the new node
    newNode=Node(e)
    #the new node must point to the current head
    newNode.next=self.head
    
    if self.isEmpty():
      self.tail=newNode
      
    #update the reference of head to point the new node
    self.head=newNode
    #increase the size of the list  
    self.size=self.size+1
    
    
  def addLast(self,e):
    """Adds a new element, e, at the end of the list"""
    #create the new node
    newNode=Node(e)
    #the last node must point to the new node
    #now, we must update the tail reference
    
    if self.isEmpty():
      self.head=newNode
    else:
      self.tail.next= newNode
      
    self.tail=newNode


    #increase the size of the list  
    self.size=self.size+1
    
    
  def toString(self):
    """Returns a string with the elements of the list"""
    temp=self.head
    strList=''
    while temp is not None:
      strList=strList+','+str(temp.element)
      temp=temp.next
    return strList[1:]
    
  def removeFirst(self):
    """Removes the first element of the list"""
    if self.isEmpty():
      print('Error: list is empty!')
      return None
    
    #gets the first element, which we will return later
    first=self.head.element
    #updates head to point to the new head (the next node)
    self.head=self.head.next
    #if the list only has one node, tail must be None
    if self.isEmpty():
      self.tail=None
    self.size=self.size-1
    
    return first
    
  def removeLast(self):
    """Removes and returns the last element of the list"""
    if self.isEmpty():
      print('Error: list is empty!')
      return None

    last=self.tail.element

    #we need to reach the penultimate node
    previous=None
    current=self.head
    while current.next is not None:
        previous=current
        current=current.next
    
    if previous is None:
      self.head=None
    else:
      previous.next=None
    
    self.tail=previous 
    
    self.size=self.size-1
  
    return last
  

    
    
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
    
    
  def insertAt(self,index,e):
    """This methods inserts a new node containing the element e at the index
    position in the list"""
    
    #first, we must check that index is a right position. Note that index=size
    #is a right position for the insertAt method. 
    if index<0 or index>self.size:
      print(index, 'Error: index out of range')
      return 
   
  
    if index==0:
      self.addFirst(e)
    elif index==self.size:
      self.addLast(e)
    else:
      #we need to reach the previous node (the node at the index-1 position)
      i=0
      previous=self.head
      while i<index-1:
        previous=previous.next
        i=i+1

      #now, previous is the node with index-1
      #create the new node
      newNode=Node(e)
      #newnode must point to the node after previous (which is previous.next)
      newNode.next = previous.next
      #previous must point with its next reference to the new node
      previous.next = newNode
      self.size += 1

      
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
      #we must to reach the node before the node at the index position
      i=0
      previous=self.head
      while i<index-1:
        previous=previous.next
        i=i+1
      
      #previous is the node at index -1 position
      
      
      previous.next = previous.next.next
      self.size=self.size-1

"""Once you have implemented the two classes, you can use them in order to create your own lists:"""

L=SinglyLinkedList2()
print("list:",L.toString())


L.addFirst(5)
L.addFirst(3)
L.addFirst(2)
L.addFirst(1)


#it should returns 1,2,3,5
print("list:",L.toString())
L.addLast(0)
print('after addLast(0)')
#it should returns 1,2,3,5,0
print("list:",L.toString())

L.removeFirst();
print('after removeFirst')

#it should returns 2,3,5,0
print("list:",L.toString())

L.removeLast();
print('after removeLast')
#it should returns 2,3,5
print("list:",L.toString())


for i in range(L.size):
  print("L.getAt({})={}".format(i,L.getAt(i)))

L.getAt(7)
  
L.insertAt(0,1)
#it should returns 1,2,3,5
print("list:",L.toString())

L.insertAt(L.size,6)
#it should returns 1,2,3,5,6
print("list:",L.toString())
L.insertAt(L.size,7)
#it should returns 1,2,3,5,6,7
print("list:",L.toString())

L.insertAt(-10,0)
L.insertAt(L.size+1,0)

L.removeAt(-1)
L.removeAt(L.size)

L.removeAt(0)
#it should returns 2,3,5,6,7
print("list:",L.toString())
L.removeAt(L.size-1)
#it should returns 2,3,5,6
print("list:",L.toString())
L.removeAt(2)
#it should returns 2,3,6
print("list:",L.toString())

while L.isEmpty() == False:
  print(L.removeLast())
  
for i in range(5):
  L.addFirst(i)
  
print("list:",L.toString())