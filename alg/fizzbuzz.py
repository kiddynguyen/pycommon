#!/usr/bin/python -tt

def fizzbuzz(max_num):
  for num in range(max_num):
    if num % 3 == 0:
      if num % 5 == 0:
        print 'fizzbuzz'
      else:
        print 'fizz'
    elif num % 5 == 0:
      print 'buzz'
    else:
      print num

  return

def main():
  fizzbuzz(20)

if __name__ == '__main__':
  main()
