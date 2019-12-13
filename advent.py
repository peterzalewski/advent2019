#!/usr/bin/env python

def calculate_fuel_requirement(mass):
  assert(mass > 0)
  return (mass // 3) - 2

def day1():
  with open('day1/input.txt', 'r') as module_weights:
    return sum(calculate_fuel_requirement(int(mass)) for mass in module_weights)

if __name__ == '__main__':
  print(day1())
