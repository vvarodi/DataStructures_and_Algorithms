
from doublylinkedlist import DoublyLinkedList

def checkPalindrome(word):
  l=DoublyLinkedList()
  for c in word:
    l.addLast(c)
    
  left=l.head
  right=l.tail
  size=l.size
  i=0
  print(size)
  while i<size//2:
    if left.element!=right.element:
      return False
    i+=1
    left=left.next
    right=right.prev
    
  return True

word='a'
print(word,checkPalindrome(word))
      
word='ab'
print(word,checkPalindrome(word))
      
word='anna'
print(word,checkPalindrome(word))
      
word='level'
print(word,checkPalindrome(word))
      
word='12 3 21'
print(word,checkPalindrome(word))