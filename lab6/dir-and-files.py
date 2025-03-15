# # 1
import os
# path1='C:/Users/Darya/Downloads/KBTU/PP2/labs'
# print("All directories and files: ")
# print([i for i in os.listdir(path1)])
# print("Only directories: ")
# print([i for i in os.listdir(path1) if os.path.isdir(os.path.join(path1, i))])
# print("Only files: ")
# print([i for i in os.listdir(path1) if not os.path.isdir(os.path.join(path1, i))])

# # 2
# path2='C:/Users/Darya/Downloads/KBTU/PP2/labs/lab6'
# print(f'''
# Exists: {os.path.exists(path2)},
# Readable: {os.access(path2, os.R_OK)},
# Writable: {os.access(path2, os.W_OK)},
# Executable: {os.access(path2, os.X_OK)}
# ''')

# # 3
# path3='C:/Users/Darya/Downloads/KBTU/PP2/labs'
# if os.path.exists(path3):
#     print([i for i in os.listdir(path3)])
# else:
#     print("path doesn't exist")

# 4
# f=open("sample.txt")
# rows=0
# if not f.read(1):
#     print(rows)
# else:
#     for i in f.read():
#         if i=="\n":
#             rows+=1
#     print(rows+1)
# f.close()

# # 5
# # f=open("sample.txt","w")
# # list1=[1,2,3,4]
# # f.write(str(list1))
# # f.close()

# # 6
# import string
# alphabet=string.ascii_uppercase
# # for i in alphabet:
# #     f=open(f"{i}.txt","x")
# #     f.close()

# # 7
# f=open("sample.txt")
# content=f.read()
# f.close()
# f=open("sample2.txt","w")
# f.write(content)
# f.close()

# 8
path8='C:/Users/Darya/Downloads/KBTU/PP2/labs/lab6/myfile.txt'
if os.path.exists(path8) and os.access(path8, os.W_OK):
  os.remove("myfile.txt")
else:
  print("The file does not exist")


