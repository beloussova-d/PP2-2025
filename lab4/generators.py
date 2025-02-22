n=int(input())
# 1
# def squares(n):
#     num=0
#     while num**2<=n:
#     # while num<=n:
#         yield num**2
#         num+=1
# list1=list(squares(n))
# print(list1)

# 2
# listeven=[i for i in range(0,n+1,2)]  #=list(i for i in range(0,n,2))
# s=str(listeven)
# print(s[1:-1])

# 3
# def divis(n):
#     num=0
#     while num<=n:
#         if num%3==0 or num%4==0:
#             yield num
#         num+=1
# list1=list(divis(n))
# print(list1)

# 4
# def squares(a,b):
#     num=a
#     while num<=b:
#         yield num**2
#         num+=1
# a=n
# b=int(input())
# for i in squares(a,b):
#     print(i)

# 5
def ntozero(n):
    num=n
    while num>=0:
        yield num
        num-=1
for i in ntozero(n):
    print(i)
