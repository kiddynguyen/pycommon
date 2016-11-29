#!/usr/bin/python -tt

def swap(list, i, j):
  list[i] = list[i] + list[j]
  list[j] = list[i] - list[j]
  list[i] = list[i] - list[j]
