#!/usr/bin/python -tt
import sys
import random
import common

def qsort(list):
  size = len(list)
  qsort_recur(list, 0, size-1)

def qsort_recur(list, left, right):
  if left == right:
    return

  pivot = left + 1
  i = pivot
  while i <= right:
    if list[i] <= list[left]:
      common.swap(list, i, pivot)
      pivot += 1
    i += 1

  common.swap(list, left, pivot-1)
  qsort_recur(list, left, pivot-1)
  qsort_recur(list, pivot, right)

def main():
  list = []
  for i in range(3):
    list.append(random.randrange(100))

  print list
  qsort(list)
  print list
  return

if __name__ == '__main__':
  main()
