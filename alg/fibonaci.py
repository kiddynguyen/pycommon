#!/usr/bin/python -tt

import sys
import random

""" Calculate fibonaci nth using iterator - Dynamic programming?
"""
def fibo(n):
  if n < 2:
    return 1

  cur = prev = 1
  pos = 2
  while pos <= n:
    cur = cur + prev
    prev = cur - prev # also can use a tmp var to keep cur
    pos += 1

  return cur

""" Calculate fibonaci nth using recursion
"""
def fibo2(n):
  if n < 2:
    return 1

  return fibo2(n-1) + fibo2(n-2)

""" Calculate fibonci nth eliminating recursion
"""
def fibo3(n):
  if n < 2:
    return 1
 
  stack = [1, 1]
  pos = 2
  while pos <= n:
    fibo_at_pos = stack[-1] + stack[-2]
    stack.append(fibo_at_pos)
    pos += 1

  return stack[-1]

def main():
  for n in range(100):
    print 'f1(' + str(n) + '):', fibo(n)
    print 'f3(' + str(n) + '):', fibo3(n)
    print 'f2(' + str(n) + '):', fibo2(n)

  return 

if __name__ == '__main__':
  main()
