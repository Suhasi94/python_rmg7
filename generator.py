"""
#### genertor ############
def func():
    for i in range(3):
        yield i
res = func()
print(next(res))
print(next(res))
l = [1,2,3,4]
def func1(a):
    for i in a:
        yield i**2
        yield i**3
    
print(list(func1(l)))
##############generator expression #########
l = [2,3,4,5]
res = ((num**2,num**3) for num in l if num%2==0)
print(next(res))
print(next(res))


s = "aaabbbbccdddertrr"
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)

dc = {i:s.count(i) for i in s}
print(dc)

l = [123,45,"hi","hello"]

d = {i:i if isinstance(i,int) else i[::-1] for i in l}
d = {key:value if statement else value for loop}
"""


# generate square numbers of given list
l = [1, 2, 3, 4]

# generate a tuple of only numeric values in the given list

items = ["flipkart", 2021, "gmail", 1.2, [1, 2, 3], 2+3j, True]

# generate only the strings with odd length in the given list

names = ["bob", "steve", "alex", "maya", "john"]

# generate a tuple of only numeric values in the given list

items = ["flipkart", 2021, "gmail", 1.2, [1, 2, 3], 2+3j, True]

# generate a list -> if individual datatype, reverse it else keep it as it is
items = ["flipkart", 2021, "gmail", 1.2, [1, 2, 3], 2+3j, True]

# Generating List of PI values with increasing decimal point numbers
#   up to user defined number

import math
PI = math.pi
print(PI)

def func(num):
    for i in range(num):
        yield round(PI,i)
print(list(func(6)))

g = (round(PI,i) for i in range(6))
print(list(g))

# 1.   A function takes variable number of positional arguments as input.
#   How to check if the arguments that are passed are more than 5

#2. "Write a generator function to print the below output.

# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX

# 3. write a generator function to generate 10 fibonacci series numbers

# 4. Python Program for How to check if a given number is Fibonacci number?

# 5.generate a list of names starting with vowels in the given string
#names = ['laura', 'steve', 'bill', 'james','greig', 'scott', 'alex', 'ive']

# 6.generate expression to sum the factorial of numbers from 1-5


# 0 1 1 2 3 5 8 13 .....


def fibo(num):
    a = 0
    b = 1
    l = []
    for i in range(num):
        yield a
        l.append(a)
        c = a + b
        a = b
        b = c
    if num in l:
        yield "its a fibo number"
    else:
        yield "its not a fibo number"
print(list(fibo(10)))


def facto(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
        yield fact
    
print(sum(list(facto(5))))
        
from math import factorial

g = (factorial(i) for i in range(1,6))
#print(sum(list(g)))
s = 0
for i in g:
    s = s + i
print(s)


data = [
    {"name": "John", "age": 30},
    {"name": "Aman", "age": 19},
    {"name": "Gita", "age": 15}
]
def function(item):
    if item["age"] > 18:
        return item["age"]

res = list(filter(function, data))
print(res)


















        























































































