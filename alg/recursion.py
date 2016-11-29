#!/usr/bin/python -tt

def factorial_iteration(n):
  if n == 0:
    return 1

  fn = 1
  i = 1
  while i <= n:
    fn *= i
    i += 1

  return fn

def factorial_recursion(n):
  if n == 0:
    return 1
  return n * factorial(n-1)

def factorial_eliminate_recursion(n):
  if n == 0:
    return 1

  stack = [1]
  i = 1
  while i <= n:
    fi = stack[-1] * i
    stack.append(fi)
    i += 1

  return stack[-1]

def main():

if __name__ == '__main__':
  main()
