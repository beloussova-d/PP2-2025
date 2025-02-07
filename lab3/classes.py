# 1) string in upper case
# class Strings:
#     def getString(self):
#         self.s=input()
#     def printString(self):
#         print(self.s.upper())
# str1=Strings()
# Strings.getString(str1)
# Strings.printString(str1)

# 2,3)
# class Shape:
#     def area(self):
#         return 0
# class Square(Shape):
#     def __init__(self,l):
#         self.length=l
#     def area(self):
#         return self.length**2
# class Rectangle(Shape):
#     def __init__(self,l,w):
#         self.length=l
#         self.width=w
#     def area(self):
#         return self.length*self.width
# sq1=Square(10)
# print(Square.area(sq1))
# rec1=Rectangle(2,6)
# print(Rectangle.area(rec1))

# 4)
# import math
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def show(self):
#         return f"(x;y) = ({self.x};{self.y})"
#     def move(self):
#         self.x=int(input('new x = '))
#         self.y=int(input('new y = '))
#     def dist(self, secondPoint):
#         return math.sqrt((secondPoint.x-self.x)**2+(secondPoint.y-self.y)**2)
# p1=Point(0,0)
# p2=Point(0,0)
# print("first point: "+Point.show(p1))
# print("second point: "+Point.show(p2))
# Point.move(p2)
# print(f"distance between 2 points = {p1.dist(p2)}")

# 5)
# class Account:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=balance
#     def deposit(self, sum):
#         self.balance=self.balance+sum
#         print(f"Balance = {self.balance}")
#     def withdraw(self, sum):
#         if self.balance<sum:
#             print("Error: withdrawals can't exceed the available balance")
#         else:
#             self.balance=self.balance-sum
#             print(f"Balance = {self.balance}")
# user1=Account("John", 1000)
# Account.withdraw(user1, 1500)
# Account.withdraw(user1, 500) 
# Account.deposit(user1, 300)

# 6) ummm no mention of classes..... also why lambda
# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# numbers=[2, 3, 4, 5, 6, 7, 9, 11]
# ### prime_num=list(filter(lambda x: is_prime(x),numbers))
# prime_num=list(filter(is_prime,numbers))
# print(prime_num)
