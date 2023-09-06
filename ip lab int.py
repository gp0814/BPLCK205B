#!/usr/bin/env python
# coding: utf-8

# In[6]:


name=input('Enter name:')
usn=input('Enter usn:')
m1=int(input('Enter marks of subject 1='))
m2=int(input('Enter marks of subject 2='))
m3=int(input('Enter marks of subject 3='))
total=m1+m2+m3
percent=float((total/300)*100)
print('Name=',name)
print('USN=',usn)
print('Total marks=',total)
print('Percentage=',percent,'%')
if(percent>90):
    print('Distinction')
elif(75<percent<90):
    print('First class')
elif(55<percent<75):
    print('Pass')
else:
    print('Fail')
    


# In[10]:


name=input('Enter name:')
year=int(input('Enter birth year:'))
age=2023-year
print('You are',age,'years old')
if(age>60):
    print('Senior citizen')
else:
    print('Non-senior citizen')


# In[12]:


n=int(input('Enter n:'))
series=[0,1]
for i in range(n-2):
    next=series[i]+series[i+1]
    series.append(next)
print(str(series))


# In[15]:


def fact(n):
    sum=1
    while(n>=1):
        sum=sum*n
        n=n-1
    return sum
n=int(input('Enter a value:'))
k=int(input('Enter another value:'))
bc=fact(n)/(fact(k)*fact(n-k))
print(bc)


# In[19]:


import math
N=int(input('Enter n:'))
numbers=[]
for i in range(N):
    num=float(input('Enter a number:'))
    numbers.append(num)

mean=(sum(numbers))/N
variance=sum((x-mean)**2 for x in numbers)/N
std_dev=math.sqrt(variance)
print('Mean=',mean)
print('Variance=',variance)
print('Standard deviation=',std_dev)


# In[22]:


number=input('Enter a number:')
frequency={}
for digit in number:
    if digit in frequency:
        frequency[digit]+=1
    else:
        frequency[digit]=1
print('Digit frequencies')
for digit in frequency:
    print(digit+':',frequency[digit])


# In[1]:


with open("abhi.txt","r") as file:
    text=file.read()
text=text.lower()
for p in ['.',',',':',';','(',')','?','!']:
    text=text.replace(p,' ')
words=text.split()
freq_dict={}
for word in words:
    if word in freq_dict:
        freq_dict[word]+=1
    else:
        freq_dict[word]=1
sorted_freq=sorted(freq_dict.items(),key=lambda x:x[1],reverse=True)
print('frequency')
for word,freq in sorted_freq[:10]:
    print(word+':',str(freq))


# In[14]:


class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,other):
        return Complex(self.real+other.real,self.imag+other.imag)
def add_complex_numbers(c1,c2):
    return c1+c2
numbers=[]
n=int(input('enter n:'))
for i in range(n):
    print(f'enter the complex number{i+1}')
    real=int(input('Real part:'))
    imag=int(input('Imag part:'))
    numbers.append(Complex(real,imag))
result=numbers[0]
for i in range(1,n):
    result=add_complex_numbers(result,numbers[i])
print(f'sum:{result.real}+{result.imag}i')


# 

# In[19]:


class student:
    def __init__(self,name,usn):
        self.name=name
        self.usn=usn
        self.marks=[0,0,0]
        self.total=0
    def getMarks(self):
        for i in range(3):
            self.marks[i]=int(input(f'enter marks for sub{i+1}:'))
        self.total=sum(self.marks)
    def display(self):
        print('Scorecard:')
        print('Name:',self.name)
        print('USN:',self.usn)
        print('Marks:')
        for i in range(3):
            print(f'Subject {i+1}:{self.marks[i]}')
        print('Total:',self.total)
        print('Percentage:',(self.total/300)*100,'%')
name=input('Enter name:')
usn=input('Enter usn:')
s=student(name,usn)
s.getMarks()
s.display()


# In[23]:


def DivExp(a,b):
    assert a>0,'a must be greater than zero'
    if b==0:
        raise Exception('b cannot be zero')
    else:
        c=a/b
        return c
a=int(input('Enter a:'))
b=int(input('Enetr b:'))
try:
    result=DivExp(a,b)
    print(f'{a}/{b}={result}')
except AssertionError as e:
    print(f'Assertion error={e}')
except Exception as e:
    print(f'Exception:{e}')


# In[6]:


import os 
import sys
import pathlib
import zipfile
dirName=input('Enter directory name that u want to backup:')
if not os.path.isdir(dirName):
    print("Directory",dirName,"doesnt exist")
    sys.exit(0)
curDirectory=pathlib.Path(dirName)
with zipfile.ZipFile('myZip.zip',mode="w") as archive:
    for file_path in curDirectory.glob("*"):
        archive.write(file_path,arcname=file_path.relative_to(curDirectory))
if os.path.isfile("myZip.zip"):
    print("Archive","myZip.zip","created successfully")
else:
    print('error')


# In[ ]:




