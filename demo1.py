#encoding:utf8
#@Time      :2019/12/4 21:45
#@Author    :DRAGON
#@File      :demo1.py
#@Software  :PyCharm

#sum 1-100

def sum():
    sum=0
    n = 1
    for n in range (1, 101):
        sum = sum + n
    return sum
print(sum())

#=================

def sum():
    sum =0
    x = 1
    while x<=100:
        sum = sum + x
        x += 1
    return sum
print(sum())

#================
from functools import reduce
def sum(x,y):
    return x+y
print(reduce(sum, range(1, 101)))

#=============