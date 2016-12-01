#!/usr/bin/python -tt
from person import Person
from engineer import Engineer

def main():
  person = Person('minhtu', 26)
  print person
  print 'name =', person.name
  person.name = 'lamdieu'
  print person
   
  person.class_method()
   
  engineer = Engineer('tunm2', 26)
  print engineer
  person.static_method()
   
if __name__ == '__main__':
  main()
