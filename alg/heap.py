#!/usr/bin/python -tt
import random

def swap(list, i, j):
  list[i] += list[j]
  list[j] = list[i] - list[j]
  list[i] = list[i] - list[j]

def heapify(list, pos):
  last = len(list) - 1
  left = 2*pos + 1
  right = left + 1
  next_pos = pos

  if right <= last:
    next_pos = left if list[left] > list[right] else right
  elif left <= last:
    next_pos = left

  if list[pos] >= list[next_pos]:
    return

  swap(list, pos, next_pos)
  heapify(list, next_pos)

def build_heap(list):
  i = len(list) / 2
  while i >= 0:
    heapify(list, i)
    i -= 1

def main():
  list = []
  for i in range(20):
    list.append(random.randrange(100))

  print list
  build_heap(list)
  print list
  return

if __name__ == '__main__':
  main()
