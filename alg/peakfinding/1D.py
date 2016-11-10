#!/usr/bin/python -tt

import sys
import random

NITEMS = 20

def find_peak_recur(items, left, right):
  mid = (left + right) / 2
  if (mid == left or items[mid] >= items[mid-1]) and (mid == right or items[mid] >= items[mid+1]):
    return items[mid]

  if items[mid] < items[mid-1]:
    return find_peak_recur(items, left, mid-1)
  else:
    return find_peak_recur(items, mid+1, right)

def find_peak(items):
  return find_peak_recur(items, 0, len(items)-1)

def main():
  items = []
  i = 0
  while i < NITEMS:
    item = random.randrange(100)
    items.append(item)
    i += 1

  print 'items: '
  print items

  apeak = find_peak(items)
  print 'a peak: ', apeak

if __name__ == '__main__':
  main()
