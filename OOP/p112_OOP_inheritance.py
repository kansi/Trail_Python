#!/usr/bin/env python

# This module explains the concept of inheritance in OOP python
# Code is taken from : http://www.freenetpages.co.uk/hp/alan.gauld/tutclass.htm

# The following code implements bank accounts where we can deposit cash,
# obtain the balance and make a withdrawal. Some of the accounts provide interest
# and others charge fees for withdrawals.
class BalanceError(Exception):
  value = "Sorry you only have $%6.2f in your account"

class BankAccount:
  def __init__(self, initialAmount):
    self.balance = initialAmount
    print "Account created with balance %5.2f" % self.balance

  def deposit(self, amount):
    self.balance = self.balance + amount

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance = self.balance - amount
    else:
      raise BalanceError, BalanceError.value % self.balance

  def checkBalance(self):
    return self.balance

  def transfer(self, amount, account):
    try:
      self.withdraw(amount)
      account.deposit(amount)
    except BalanceError:
      print BalanceError.value

a = BankAccount(500)
a.withdraw(100)
print "A = ", a.checkBalance()

# Now we use inheritance to provide accounts that adds interest (let interest
# be 3% ) on every deposit and accounts that change on withdrawl ($3). Notice
# that when we inherit from a class in python, we write the parent class in
# brackets. We can override the methods of the parent class in the child class
# as can be seen below.
class InterestAccount(BankAccount):
  def deposit(self, amount):
    BankAccount.deposit(self,amount)
    self.balance = self.balance * 1.03

# Notice below that we have called the __init__ of the parent inside the
# __init__ of the child class and also created a new "fee" variable.
class ChargingAccount(BankAccount):
  def __init__(self, initialAmount):
    BankAccount.__init__(self, initialAmount)
    self.fee = 3

  def withdraw(self, amount):
      BankAccount.withdraw(self, amount+self.fee)

# Interest account
c = InterestAccount(1000)
c.deposit(100)
print "C = ", c.checkBalance()


# Charging account
d = ChargingAccount(300)
d.deposit(200)
print "D = ", d.checkBalance()
d.withdraw(50)
print "D = ", d.checkBalance()
d.transfer(100,a)
print "A = ", a.checkBalance()
print "D = ", d.checkBalance()

