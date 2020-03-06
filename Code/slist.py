# -*- coding: utf-8 -*-
"""
Implementación TAD Lista usando una lista simplemente enlazada
"""

class SNode:
  def __init__(self,e,next=None):
    self.elem=e
    self.next=next

class SList:
  def __init__(self):
    self.head=None
    self.size=0

  def addFirst(self,e):
    newNode=SNode(e)
    newNode.next=self.head
    self.head=newNode
    self.size +=1

  def isEmpty(self):
    return self.size==0

  def __len__(self):
    return self.size

  def addLast(self,e):
    if self.isEmpty():
      self.addFirst(e)
    else:
      newNode=SNode(e)
      nodeIt=self.head
      while nodeIt.next!=None:
        nodeIt=nodeIt.next
      nodeIt.next=newNode
      self.size +=1


#  def addLast(self,e):
#    if self.isEmpty():
#      self.addFirst(e)
#    else:
#      newNode=SNode(e)
#      nodeIt=self.head
#      for i in range(1,self.size):
#        nodeIt=nodeIt.next
      #nodeIt is the last node
#      nodeIt.next=newNode
#      self.size +=1


  def removeFirst(self):
    result=None
    if self.isEmpty():
      print("List is emtpy!!!")
    else:
      result=self.head.elem
      self.head=self.head.next
      self.size-=1
      
    return result

  def removeLast(self):
    result=None
    if self.isEmpty():
      print("List is emtpy!!!")
    else:
      penult=None #will point to the penultimate node
      last=self.head #will point to the last node
      while last.next!=None:
        penult=last
        last=last.next
      
      if penult==None:
        #the list only has an element
        result=self.removeFirst()
      else:
        result=last.elem
        penult.next=None
        self.size -=1
    
    return result

  def __str__(self):
    result=''
    nodeIt=self.head
    while nodeIt!=None:
      result += str(nodeIt.elem) + ','
      nodeIt=nodeIt.next
    if len(result)>0:
      result=result[:-1]
    return result




#  def removeLast(self):
#    result=None
#    if self.isEmpty():
#      print("List is emtpy!!!")
#    elif self.size==1:
#      result=self.removeFirst()
#    else:
#      nodeIt=self.head
#      while nodeIt.next.next!=None:
#        nodeIt=nodeIt.next
      #nodeIt is the penultimate node of the list
#      last=nodeIt.next
#      result=last.elem
#      nodeIt.next=None
#      self.size -=1
#    return result

import random 
l=SList()
for i in range(1,10):
  #l.addLast(random.randint(0,10))
  l.addLast(i)
print(str(l))
l.addFirst(0)
print(str(l))
print(l.removeLast())
print(str(l))
print(l.removeLast())
print(str(l))

while len(l)>0:
  print(l.removeLast())

print(l.removeLast())