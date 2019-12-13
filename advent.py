#!/usr/bin/env python

def calculate_fuel_requirement(mass):
  if mass <= 0:
    return 0

  fuel_mass = max(0, (mass // 3) - 2)
  return fuel_mass + calculate_fuel_requirement(fuel_mass)

def day1():
  with open('day1/input.txt', 'r') as module_masses:
    return sum(calculate_fuel_requirement(int(mass)) for mass in module_masses)

if __name__ == '__main__':
  print(day1())
