# -*- coding: utf-8 -*-

class CreditCard:
  """The CreditCard class provide a simple model, a template for credit cards. 
A credit card must contain information about the customer, account number, credit limit, and
current balance."""

  def __init__ (self, name, idCard, limit):
    """Creates a new credit card object"""
    self._customer=name #the name of the customer 
    self._idCard=idCard #the id of the credit card 
    self._limit=limit   #credit limit
    self._balance=0     #the initial balance is 0
 
 
  def charge(self, price):
    """Charge the price to the balance of the card. 
    Must check if there is enough credit. Return True
    if the charge was processed, False if charge was denied"""
    # if charge would exceed limit,
    if price + self._balance > self._limit:
      print('charge denied')
    else:
      self._balance = self._balance + price
    

    
  def make_deposit(self, amount):
    """Make a deposit (add money to the credit card). 
    Reducs the balance"""
    
    self._balance = self._balance - amount
    
    if self._balance<0:
      print('Balance cannot be negative')
      self._balance=0
      
        
  def __str__(self):
      result='Customer:'+self._customer
      result += ' id card:' +self._idCard
      result += ' Limit:'+str(self._limit)
      result += ' Balance:'+str(self._balance)
      return result

"""Now, we create an instance of a credit card and try each method."""
#if __name__ == '__main__':
#    #Create an instance of the credit card
#    cc1 = CreditCard('Isabel Segura','5391 0375 9387 5309', 3000 )
#    print(str(cc1))
#    #we make a charge 
#    cc1.charge(2000)
#    print(str(cc1))
#    #we make a deposit
#    cc1.make_deposit(1000)
#    print(str(cc1))
#    
#    cc1.charge(2500)
#    print(str(cc1))