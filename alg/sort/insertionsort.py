#!/usr/bin/python -tt

import random
import common

SIZE = 20

def isort(list):
  i = 1
  size = len(list)
  while i < size:
    j = i - 1
    current = list[i]
    while j >= 0 and current < list[j]:
      list[j+1] = list[j]
      j -= 1
    list[j+1] = current
    i += 1
  
  return

""" Optimize for the case comparing operation is expensive
 Use binary search instead of comparing each items
"""
def binary_isort(list):
  i = 1
  size = len(list)
  while i < size:
    current = list[i]
    pos = binary_search(list, 0, i-1, current)
    j = i
    while j > pos:
      list[j] = list[j-1]
      j -= 1
    list[pos] = current
    i += 1

  return

""" Return position of the most same item
"""
def binary_search(list, left, right, value):
  if left == right:
    return left

  mid = (left + right) / 2
  if list[mid] < value:
    return binary_search(list, mid+1, right, value)
  elif list[mid] > value:
    return binary_search(list, left, mid, value)
  else:
    return mid

def main():
  # init lists
  list1 = []
  list2 = []
  for i in range(SIZE):
    num = random.randrange(100)
    list1.append(num)
    list2.append(num)
  
  print 'original list:'
  print list1

  # sort list by normal insertion sort
  isort(list1)
  print 'sorted list by normal insertion sort:'
  print list1

  # sort list by binary insertion sort
  binary_isort(list2)
  print 'sorted list by binary insertion sort:'
  print list2

  # test binary search
  found = binary_search(list1, 0, len(list1)-1, 20)
  print 'found by binary search', found

  return

if __name__ == '__main__':
  main()
