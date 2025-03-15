#1
import math
list1=[1,2,3,4]
print(math.prod(list1))

#2
s1="HeLlO"
upper=sum(1 for i in s1 if i.isupper())
lower=sum(1 for i in s1 if i.islower())
print(upper, lower)

#3
txt1="Text"
txt2="txt"
print((txt1==txt1[::-1]),(txt2==txt2[::-1]))

#4
import time
n=int(input())
ms=int(input())
time.sleep(ms/1000)
print(f"Square root of {n} after {ms} miliseconds is {math.sqrt(n)}")

#5
t1=(0,True,1,"a")
t2=(True,1,1)
print(all(t1), all(t2))