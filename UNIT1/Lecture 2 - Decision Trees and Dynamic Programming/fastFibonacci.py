# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 12:12:01 2017

@author: Administrator
"""
def fib(n):
    '''
    Return Fibnpcci of n
    '''
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
#for i in range(121):
#    print('fib(' + str(i) + ') = ', fib(i))

def fastFib(n, memo = {}):
    '''
    Assume n is an int >= 0, memo used only by recursive calls
    Return Fibonacci of n
    '''
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result
    
#for i in range(121):
#    print('fib(' + str(i) + ') = ', fastFib(i))