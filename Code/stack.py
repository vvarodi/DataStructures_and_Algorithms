#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Stack1:
  """LIFO Stack implementation using a Python list as storage. 
  The top of the stack stored at the end of the list."""
  
  def __init__(self):
    """Create an empty stack"""
    self.items=[]
    
  def __len__(self):
    """Return the number of elements in the stack"""
    return len(self.items)
  
  def isEmpty(self):
    """Return True if the stack is empty"""
    return len(self.items)==0
  
  def __str__(self):
    #print the elements of the list
    return str(self.items)


  def push(self,e):
    """Add the element e to the top of the stack"""
    self.items.append(e)
    
  def pop(self):
    """Remove and return the element from the top of the stack"""
    if self.isEmpty():
      print('Error: Stack is empty')
      return None
    
    return self.items.pop() #remove last item from the list
  
  def top(self):
    """Return the element from the top of the stack"""
    if self.isEmpty():
      print('Error: Stack is empty')
      return None
    
    #returns last element in the list
    return self.items[-1] 
  
    
"""## Second option: top at the first position of the list```
#
#We could have chosen to implement the stack using a list where
#the top is at the beginning instead of at the end. In this case, the previous pop and append methods would no longer work and we would have to index position 0 (the first item in the
#list) explicitly using pop and insert. The implementation is shown below.
#"""

class Stack2:
  """LIFO Stack implementation using a Python list as storage. 
  The top of the stack is stored at the beginning of the list."""
  def __init__(self):
        self.items = []
      
  #tests if the stack is empty
  def isEmpty(self):
    return self.items == []


  def __len__(self):
    return len(self.items)

  def __str__(self):
    return str(self.items)


  #adds at the beginning of the list
  def push(self, item):
    self.items.insert(0,item)

  #removes and returns the top element
  def pop(self):
    if self.isEmpty():
      print('Error: Stack is empty')
      return None
    
    #return the first element
    return self.items.pop(0)
    
  #returns the top element
  def top(self):
    if self.isEmpty():
      print('Error: Stack is empty')
      return None
    
    return self.items[0]


"""**What implementation is better? **
Althought the above implementations are logically equivalent, the first one is better 
than the second one because they operations append and pop() operations are both O(1), 
while insert(0) and pop(0) have linear complexity (O(n) for a stack of size n). 
In other words, the second implementation (top element is stored at 
the fist position of the list) requires more time complexity 
than the first one (where the top element is stored at the end of the list). 
"""

test1=False  #set  to True to test Stack1
if test1:
    print('testing Stack1')
    s=Stack1()
    print('isEmpty()',s.isEmpty())
    s.push('W')
    s.push('O')
    print('top element',s.top())
    print('isEmpty()',s.isEmpty())
    s.push('R')
    s.push('D')
    print('Content of stack',str(s))
    print('pop:',s.pop())
    print('Content of stack',str(s))
    print('top element:',s.top())

test2=False #set  to True to test Stack2
if test2:
    print('testing Stack2')
    s=Stack2()
    print('isEmpty()',s.isEmpty())
    s.push('W')
    s.push('O')
    print('top element',s.top())
    print('isEmpty()',s.isEmpty())
    s.push('R')
    s.push('D')
    print('Content of stack',str(s))
    print('pop:',s.pop())
    print('Content of stack',str(s))
    print('top element:',s.top())

 
print()
#
#"""# Using stacks for solving problems
#
#Now we will see how stacks can be used to solve real computer science problems. 
#
### Reversing words with Stack
#
#Implement a Python function that takes a string and returns its reverse string.
#"""
#
def reverse(word):
  """Returns the reverse word of the input word.
  It uses a stack"""
  s=Stack1()
  #push each character onto the stack
  for c in word:
    s.push(c)
    
  #variable for reverse word
  reWord=''
  while not s.isEmpty():
    #pop from the stack
    c=s.pop()
    #append at the end of the reverse word
    reWord=reWord+c
    
  return reWord

testReverse=False  #set  to True to test reverse
if testReverse:
    w='horse'
    print('reversing {}={}'.format(w,reverse(w)))
    w='amor'
    print('reversing {}={}'.format(w,reverse(w)))
    w='radar'
    print('reversing {}={}'.format(w,reverse(w)))


#
##"""## Balanced parenthesis
##
##
##Detecting when the parenthesis in an expression are correctly balanced or not is an important task to recognize many programming language structures (i.e. to evaluate arithmetic or logical expressions).
##
##
##In logical and arithmetic expressions, parentheses must appear in a balanced way. In other words:
##- 1) each opening symbol has a corresponding closing symbol and 
##- 2) the pairs of parentheses are properly nested. 
##
##The following table shows examples of balanced and non balanced expressions of parenthesis:
##
##| Balanced  | Non balanced |
##| --- | --- | 
##| (()()()()) | ((((((())|
##|(((()))) | ())) |
##| (()((())())) | (()()(()|
##
##
##Please, write a Python program that reads a string of parenthesis and determines if its parenthesis are balanced. 
##A stack is a good data structure to solve this problem because  closing symbols match opening symbols in the reverse order of their appearance. 
##
##
##Below, we explain the steps to implement the algorithm. Firstly, you must create an empty stack, which be used to store the opening symbols. Then, you must read the expression from left to right. For each symbol:
##- If the symbol is an opening symbol, add it on the stack (with push operation).
##- If the symbol is a closing symbol:
##    - If the stack is empty, there is no any opening symbol for it, so return false (the expression is not balanced). 
##    - Otherwise, remove the top of the stack (with pop) and continue. 
##        
##When you have read all characters in the expression, there  are two possibilities:
##a) The stack is not empty, which means that the expressions contained some opening symbols without their corresponding closing symbols. Therefore, you must return false. 
##b) The stack is empty. You must return true.
##"""
##
def balanced(exp):
    """Checks if the parenthesis in exp are balanced"""
    
    s=Stack1()
    for c in exp:
      if c=='(':
        s.push(c)
      elif c==')':
        if s.isEmpty():
          return False
        else:
          s.pop()
      else:
        #ignore any other character
        continue
      
    return s.isEmpty()
  
testBal=True
if testBal:
    print('((((((())',balanced('((((((())'))
    print('(()()()())',balanced('(()()()())'))
    print('(((())))',balanced('(((())))'))
    print('()))',balanced('()))'))
    print('(()()(()',balanced('(()()(()')      )
    print('(()((())()))',balanced('(()((())()))')      )