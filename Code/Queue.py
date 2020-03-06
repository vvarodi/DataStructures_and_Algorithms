# -*- coding: utf-8 -*-


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
  
  def __str__(self):
    strQ=''
    for x in self.items:
      strQ=strQ+','+str(x)
    #print the elements of the list
    return strQ[1:]
  
  
q=Queue()
print('isEmpty()',q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print('Content of queue',str(q))
print('front (first) element',q.front())
print('isEmpty()',q.isEmpty())
print('dequeue():',q.dequeue())
print('Content of queue',str(q))
print('front element:',q.front())
print('size:',len(q))

"""Now, we implement the function for the Josephus problem:"""

def josephus(num, k):
  q=Queue()
  #saved soldiers into the queue.
  for i in range(1,num+1):
    q.enqueue(i)
    
  while len(q)>1:
    count=1
    #k-1 dequeue/enqueue operations
    while count<k:
      q.enqueue(q.dequeue())
      count=count+1
    #kill the kth soldier
    print(str(q.dequeue()) + ' was killed')
    
  
  print('Surviving position: ' + str(q.front()))

  
josephus(40,5)