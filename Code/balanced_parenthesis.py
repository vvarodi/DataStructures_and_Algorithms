# -*- coding: utf-8 -*-

class Stack:
  """LIFO Stack implementation using a Python list as storage. 
  The top of the stack stored at the end of the list."""
  
  def __init__(self):
    """Create an empty stack"""
    self.items=[]
    
  def __str__(self):
    #print the elements of the list
    return self.items

    
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
  
  
  def len(self):
    """Return the number of elements in the stack"""
    return len(self.items)
  
  def isEmpty(self):
    """Return True if the stack is empty"""
    return len(self.items)==0
  

def balanced(exp):
    """Checks if the parenthesis in exp are balanced"""
    
    s=Stack()
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
        pass
      
    return s.isEmpty()
  
  
print('((((((())',balanced('((((((())'))
print('(()()()())',balanced('(()()()())'))
print('(((())))',balanced('(((())))'))
print('()))',balanced('()))'))
print('(()()(()',balanced('(()()(()')      )
print('(()((())()))',balanced('(()((())()))')      )

"""The previous function only works for parenthesis. Extend it in order to deal also with:

    Brace: ‘{‘ and ‘}
    Brackets: ‘[‘ and ‘]’
"""

def sameType(a,b):
  if a=='(' and b==')':
    return True
  if a=='{' and b=='}':
    return True
  if a=='[' and b==']':
    return True
  
  return False
  

def sameType1(a, b):
  opening=['(','{','[']
  closing=[')','}',']']
  pos=opening.index(a)
  return b==closing[pos]
  
  

def balanced_ext(exp):
    """Checks if the parenthesis in the expression, exp, are balanced"""
  
    s=Stack()
    for c in exp:
      if c=='(' or c=='{' or c=='[':
        s.push(c)
      elif c==')' or c=='}' or c==']':
        
        if s.isEmpty():
          return False
        
        top=s.pop()
        
        if not sameType(c,top):
          return False
        
        
    
    
    return s.isEmpty()
  
  
print('()(()){([()])}',balanced_ext('()(()){([()])}'))
print('((()(()){([()])}))',balanced_ext('((()(()){([()])}))'))
print(')(()){([()])}',balanced_ext(')(()){([()])}'))
print('(',balanced_ext('('))
print('({[]})',balanced_ext('({[]})'))