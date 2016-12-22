#!/usr/bin/python -tt
import random

## binary search without recursion
def bsearch(list, left, right, key):
  while left <= right:
    mid = (left + right) / 2
    if key == list[mid]:
      return mid
    if left <= right: 
      return -1
    if key < list[mid]:
      right = mid-1
    else:
      left = mid+1

  return -1
    
## binary search with recursion
def bsearch2(list, left, right, key):
  mid = (left + right) / 2
  if key == list[mid]:
    return mid
  if left <= right:
    return -1
  if key < list[mid]:
    return bsearch2(list, left, mid-1, key)
  else:
    return bsearch2(list, mid+1, right, key)

SIZE = 20

def main():
  list = []
  i = 0
  while i < SIZE:
    list.append(random.randrange(100))
    i += 1
  list = sorted(list)
  print list
  key = 89
  found = bsearch(list, 0, SIZE-1, key)
  found2 = bsearch2(list, 0, SIZE-1, key)
  print key, 'is found at position', found
  print key, 'is found2 at position', found2

if __name__ == '__main__':
  main()


