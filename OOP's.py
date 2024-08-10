#Classes AND objects.
#Why we are creating the classes and objects?
#How to create a class?
#use the keyword "Class"
# class customer:
#     pass
# #object creation
# c1 = customer()
# print(c1)
#what is __main__?
#is nothing but from which file the class is coming from

"""Attributes:- these are 2 types
1.class attribute:-come from class and these attributes accessible
by every object(common attributes)
2.object attribute-means unique attributes that can be applicable to
particular object """
#create a class
"""class customer:
     #create class attributes-->creating varaibles inside the class
     Bank_Name = "HFC Bank"
     Branch    = "Mumbai"
     State    = "Maharstra"
     IFSC    = "HFC000023"
#create a  object
c1 = customer()
c2 = customer()
#how can an object access the class attribute?
print(c1.Bank_Name)
print(c2.IFSC)"""

#create methods for class customer
#what is methods?
#methods can be created inside the class.
#Methods are nothing but creating functions inside the class.

class customer:
     #create class attributes-->creating varaibles inside the class
     Bank_Name = "HFC Bank"
     Branch    = "Mumbai"
     State    = "Maharstra"
     IFSC    = "HFC000023"
     """Before creating the object attributes we need initiate object
        attributes inside the class"""
     def __init__(self,name,age,intial_amount,acc_No):
          #what is __init__?
          """When you create an object by default it runs with init
             method-->initialisation method"""
          self.name = name
          self.age = age
          self.intial_amount = intial_amount
          self.acc_No = acc_No
     #creating methods
     def welcome(self):
          print(f"hello {self.name} and welcome to {self.Bank_Name}, {self.Branch}")
     def check_balance(self):
          print(f'your current balance is {self.intial_amount}')
     def deposit(self,amount):
          self.intial_amount += amount  #--> intial_amount = intial_amount + amount
          print(f"Transaction is completed."
                f'{amount} has been credited to your {self.acc_No}.'
                f"The Updated balance is {self.intial_amount}")
     def withdraw(self,amount):
          if amount <= self.intial_amount:
               self.intial_amount -= amount
               print(f"Transaction is completed."
                     f'{amount} has been deduct from your {self.acc_No}.'
                     f"The Updated balance is {self.intial_amount}")
          else:
               print("insufficient balance")
               self.check_balance()

#create a  object
c1 = customer("Python", 28,10000,123456789)
c2 = customer("shahul",28,10000,987654421)
#c2 = customer()
#How can we access the particular methods
# c1.welcome()
# c1.check_balance()
#c1.deposit(10000)
# c1.withdraw(20000)
c2.withdraw(5000)
#how can an object access the class attribute?
# print(c1.Bank_Name)
#print(c2.IFSC)
#how can an object access object attributes
# print(c1.intial_amount)

#what is self ?
#its a extra parameter in the method defination
#class.method(object)
#self act as a pointer/ reference to access the object.
