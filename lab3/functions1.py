# 1)
# def grams_to_ounces(grams):
#     ounces=28.3495231*grams
#     return ounces
# a=float(input())
# print(grams_to_ounces(a))

# 2)
# def temp_convert(F):
#     C = (5 / 9) * (F - 32)
#     return C
# F=float(input())
# print(temp_convert(F))

# 3) загадка
# def solve(numheads, numlegs):
#     rabbits=numlegs/2-numheads
#     chickens=numheads-rabbits
#     print(f"{rabbits:.0f} rabbits, {chickens:.0f} chickens")
# h=int(input())
# l=int(input())
# solve(h,l)

# 4) возвращает только prime
# def filter_prime(l):
#     for j in l:
#         prime=True
#         for i in range(2,max(l)):
#             if j==1 or j%i==0 and i!=j:
#                 prime=False
#         if prime:
#             print(j)
# listOfNum=[int(listOfNum) for listOfNum in input().split()]
# filter_prime(listOfNum)

# 5) all permutations of the string
# from itertools import permutations 
# def str_permut(s):
#     perm=permutations(s)
#     for i in perm:
#         print("".join(i))
# s=input()
# str_permut(s)


# 6) words reversed: We are ready -> ready are We
# def reverse_string(words):
#     words.reverse()
#     print(*words)
# words=input().split()
# reverse_string(words)

# 7) 3, 3 somewhere in the list
# def has_33(nums):
#     for i in range(1,len(nums)-1):
#         if nums[i]==3 and (nums[i-1]==3 or nums[i+1]==3):
#             return True
#     return False
# nums=[int(nums) for nums in input().split()]
# print(has_33(nums))

# 8)
# def spy_game(nums):
#     spy_list=[0,0,7]
#     j=0
#     for i in range(0,len(nums)):
#         if nums[i]==spy_list[j] and j!=2:  #len(spy_list)-1
#             j=j+1
#     if j==2:
#         return True
#     return False
# nums=[int(nums) for nums in input().split()]
# print(spy_game(nums))

# 9)
# import math
# def volume(R):
#     V=4/3*math.pi*R**3
#     return V
# R=float(input())
# print(volume(R))

# 10) set, but w/o set
# list1=input().split()
# list2=[]
# list2.append(list1[0])
# for i in range(0,len(list1)):
#     unique=True
#     for j in range(0,len(list2)):
#         if list2[j]==list1[i]:
#             unique=False
#     if unique: 
#         list2.append(list1[i])
# print(list2)
    

# 11
# def palindrome_check(s):
#     s=s.replace(" ","")
#     s=s.lower()
#     s1=s[::-1]
#     if s1==s:
#         print("palindrome")
#     else:
#         print("not palindrome")
# s=input()
# palindrome_check(s)

# 12 *****
# def histogram(ints):
#     for i in ints:
#         for j in range(0,int(i)):
#             print("*",end='')
#         print('')
# ints=input().split()
# histogram(ints)

# 13
# import random
# def guessing():
#     print("Take a guess.")
#     guess=int(input())
#     return guess
# print("Hello! What is your name?")
# name=input()
# num=random.randrange(1,20)
# cnt=0
# print("\nWell, "+name+", I am thinking of a number between 1 and 20.")
# while(True):
#     cnt=cnt+1
#     guess=guessing()
#     if guess==num:
#         print(f"\nGood job, {name}! You guessed my number in {cnt} guesses!")
#         break
#     elif guess<num:
#         print("\nYour guess is too low.")
#     else:
#         print("\nYour guess is too high.")
    