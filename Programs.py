#Reverse a String:
#
# a="Abishek"
# for i in a[::-1]:
#     print(i,end='')

#Vowels in a String:

# a="Abishek"
#
# a=a.lower()
# for i in a:
#     if i in 'aeiou':
#         print(i)

#remove space from sentence

# a='Abishek is a good boy'
#
# b=''
#
# for char in a:
#     if char!=' ':
#         b+=char
# print(b)

#String plaindrome:

# a='Madam'
#
# a=a.lower()
# b=a
# c=''
#
# for i in a[::-1]:
#     c+=i
#
# if b==c:
#     print(True)
#     print(c)
# else:
#     print(False)

#Find the Frequency of Characters

# string = "character frequency"
#
# frequnecy={}
#
# for char in string:
#     if char!=' ':
#         if char in frequnecy:
#             frequnecy[char]+=1
#         else:
#             frequnecy[char]=1
# for char,count in frequnecy.items():
#     print(char,count)

# Check if a String Contains Only Digits

# a="1234"
#
# digit=True
#
# for char in a:
#     if char <'0' or char >'9':
#         digit=False
#         break
# if digit:
#     print("The string contains only digit")
# else:
#     print("Also contains Alpha number")

#Replace a Substring in a String

# string = "I like Python programming"
# old_sub = "Python"
# new_sub = "Java"
# result = ""
# i=0
#
# while i<len(string):
#     if string[i:i+len(old_sub)]==old_sub:
#         result+=new_sub
#         i+=len(new_sub)
#     else:
#         result+=string[i]
#         i+=1
# print(result)

# a=['Abi','Dp']
# b=['Dp']
#
# c=set(a).intersection(set(b))
# print

# a = ['Abi', 'Dp']
#
# for i in range(len(a)):
#     if a[i]=='Abi':
#         a[i]=('Abu')
#         print(a[i])
# print(a)

# palindrome

# a=124
#
# t=a
# b=0
#
# while(a>0):
#     r=a%10
#     b=b*10+r
#     a=a//10
# if(b==t):
#     print("palindrome")
# else:
#     print("Not")

# Armstrong
#
# a=153
#
# b=0
#
# t=a
#
# while(a>0):
#     r=a%10
#     b=b+(r*r*r)
#     a=a//10
#
# if b == t:
#     print(f"{t} is an Armstrong number.")
# else:
#     print(f"{t} is not an Armstrong number.")

# Factorial
#
# a=5
#
# f=1
#
# for i in range(1,a+1):
#     f=f*i
# print(f)

# Fibnacci
#
# a=0
# b=1
# t=50
#
# for i in range(t-1):
#     d=a+b
#     a=b
#     b=d
# print(d)


# prime number

# for num in range(1,100):
#
#     if num > 1:
#         count=0
#         for i in range(2,num):
#             if num%i==0:
#                 count+=1
#         if count==0:
#             print(num)
#
# a=6
# count = 0
# for i in range(2,a):
#
#     if a%i==0:
#         count+=1
# if(count==0):
#     print("Prime")
# else:
#     print("Not prime")

# a=30
# b=20
#
#
# carry= ~a & b
# a=a^b
# b=carry<<1
# print(a)


#Find the Frequency of Characters

# string = "character frequency"
#
# frequnecy={}
#
# for char in string:
#     if char!=' ':
#         if char in frequnecy:
#             frequnecy[char]+=1
#         else:
#             frequnecy[char]=1
# for char,count in frequnecy.items():
#     print(char,count)

# Highest in array

#
# a=[12,32,22,45,67,102,22,99]
#
# b=a[0]
#
# for i in a:
#     if i>b:
#         b=i
# print(b)

# Second largest
# a = [999]
#
# largest=second=float('-inf')
#
# for i in a:
#     if i>largest:
#         second=largest
#         largest=i
#     elif i>second and i!=largest:
#         second=i
# if second == float('-inf'):
#     print("Second largest not exit")
# else:
#     print(second)

# remove duplicate:

# a=[11,23,45,32,11]
#
# b=[]
#
# for i in a:
#     if i not in b:
#         b.append(i)
#
# print(b)

# a=[11,23,45,32,11]
#
# frequency={}
#
# for char in a:
#     if char in frequency:
#         frequency[char]+=1
#     else:
#         frequency[char]=1
# for char,count in frequency.items():
#     print(char,count)
#


# string Based

# reverse a string

# s = "hello"
# revserse=""
#
# for i in s:
#     revserse=i+revserse
# print(revserse)
# for i in s[::-1]:
#     print(i,end=" ")


# Check if a String is a Palindrome

# a="madaM"
# t=a
# reverse=""
# for i in a:
#     reverse=i+reverse
# if t==reverse:
#     print("palindrome")
# else:
#     print("Not palindrome")
#
# s = "hEllo worldUu"
# vowels = "aeiouAEIOU"
# v=0
# c=0
# for i in s:
#     if i in vowels:
#         v+=1
#     else:
#         c+=1
# print(v,c)
# Check if Two Strings are Anagrams
#
# s1 = "listen"
# s2 = "silent"
#
# counts = {}
# for char in s:
#     if char in counts:
#         counts[char] += 1
#     else:
#         counts[char] = 1
# print(counts)

# def isanagram(s1,s2):
#     def charcounts(s):
#         count={}
#         for i in s:
#             if i in count:
#                 count[i]+=1
#             else:
#                 count[i]=1
#         return count
#     return charcounts(s1)==charcounts(s2)
#
# s1 = "listen"
# s2 = "silent"
# print(isanagram(s1, s2))

import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password="Abishek12345#@@#",db="user")
pycon=con.cursor()
# pycon.execute('create Database user;')
# pycon.execute('create table student (name varchar(50),rollno int,class varchar(15));')
# pycon.execute('show Databases;')
# for i in pycon:
#     print(i)
# sql="Insert into student(name,rollno,class) values(%s,%s,%s);"
# val=("Deebak","016","20cs8a")
# pycon.execute(sql,val)
# con.commit()
# print(con)
# pycon.execute('create table teacher (name varchar(50),rollno int,class varchar(15));')
sql="Insert into teacher(name,rollno,class) values(%s,%s,%s);"
val=("keerthi","047","20cs8a")
pycon.execute(sql,val)
con.commit()
# pycon.execute("alter table teacher add column id int primary key auto_increment not null")

