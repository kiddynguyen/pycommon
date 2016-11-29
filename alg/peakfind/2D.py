#!/usr/bin/python -tt

import sys
import random

SIZE = 5

def print_matrix(matrix):
  for row in matrix:
    print row

""" Create matrix which has 'size' rows and 'size' columns
Data is randomized
"""
def create_matrix(size):
  matrix = []
  i = 0
  while i < size:
    row_items = []
    j = 0
    while j < size:
      item = random.randrange(10,100)
      row_items.append(item)
      j += 1
  
    matrix.append(row_items)
    i += 1

  return matrix

""" Find max item in column 'col' of matrix 'matrix'
Return row index of max item
"""
def find_max(matrix, col):
  nrows = len(matrix)
  row = 0
  row_max = row
  while row < nrows:
    if matrix[row][col] > matrix[row_max][col]:
      row_max = row
    row += 1

  return row_max

def find_peak_recur(matrix, left_col, right_col):
  mid_col = (left_col + right_col) / 2
  mid_col_max = find_max(matrix, mid_col)
  
  return 0

def find_peak(matrix):
  return find_peak_recur(matrix, 0, len(matrix)-1)

def main():
  matrix = create_matrix(SIZE)
  print_matrix(matrix)
  
  print find_max(matrix, 1)  

if __name__ == '__main__':
  main()
