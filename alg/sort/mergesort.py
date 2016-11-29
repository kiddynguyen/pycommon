#!/usr/bin/python -tt
import sys
import random

SIZE = 20

def merge(list, list1, list2):
  i = j = k = 0
  while i < len(list1) and j < len(list2): # len takes O(1)
    if list1[i] <= list2[j]:
      list[k] = list1[i]
      i += 1
    else:
      list[k] = list2[j]
      j += 1
    k += 1

  # append the rest of longer half to result
  while i < len(list1):
    list[k] = list1[i]
    i += 1
    k += 1
  while j < len(list2):
    list[k] = list2[j]
    j += 1
    k += 1

def msort(list):
  # base case
  if len(list) <= 1:
    return

  # divide the list into two halves
  mid = len(list) / 2
  list1 = list[0:mid]
  list2 = list[mid:]

  # recursively sort each halves
  msort(list1)
  msort(list2)

  # merge two sorted lists
  merge(list, list1, list2)

def main():
  # create a randomized list
  list = []
  for i in range(SIZE):
    num = random.randrange(100)
    list.append(num)

  print 'original list'
  print list

  msort(list)
  print 'sorted list'
  print list

if __name__ == '__main__':
  main()
