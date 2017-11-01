#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python 慣用語練習

http://seanlin.logdown.com/
Created on Wed Nov  1 21:47:51 2017

@author: ihong
"""
#%%
t = '1',2,'3'
x,y,z = t

foo = lambda logging:(1 if logging else 0)
sql = (
       "select top 10 * from "
       "where ...."
       "and ..."
)
print(sql)

#%%
for n in range(2, 10):
    
    for x in range(2, n):
        if n % x == 0:
            print(n,'equals',x,'*', n/x)
            break
    else:
        print(n, 'is a prime number')
#%%
def f(a,L=None):
    if not L :
        L = []
    L.append(a)
    return(L)
    
#def f(a, L=[]):
#    L.append(a)
#    return L
    
#%%
def fib(n, memo={}):
    if n < 2:
        return 1
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]    

def fib2(n):
    if n<2:
        return 1
    else:
        return fib2(n-1) + fib(n-2)
    
#%%
#property 
RATE = 1.5
class Egg(object):

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price * RATE
    
    @price.setter
    def price(self, value):
        self._price = value
#%% 
# =============================================================================
#  proerty       
# =============================================================================
class Student:
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 and 100')
        self._score = value

        
s = Student()        
s.score = 100
