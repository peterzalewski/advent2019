#!/usr/bin/env python

INTCODE_ADD = 1
INTCODE_MULTIPLY = 2
INTCODE_STOP = 99

def day2():
  with open('day2/input.txt', 'r') as intcode:
    opcodes = [int(code) for code in next(intcode).split(',')]

  # Introduce "1202 program" error
  opcodes[1] = 12
  opcodes[2] = 2

  i_p = 0
  while opcodes[i_p] != INTCODE_STOP:
    instruction = opcodes[i_p]
    if instruction == INTCODE_ADD:
      left, right, dest = opcodes[i_p + 1:i_p + 4]
      opcodes[dest] = opcodes[left] + opcodes[right]
    elif instruction == INTCODE_MULTIPLY:
      left, right, dest = opcodes[i_p + 1:i_p + 4]
      opcodes[dest] = opcodes[left] * opcodes[right]
    elif instruction == INTCODE_STOP:
      # How did we get here?
      break
    else:
      raise NotImplementedError(instruction)

    i_p += 4

  return opcodes[0]

def calculate_fuel_requirement(mass):
  if mass <= 0:
    return 0

  fuel_mass = max(0, (mass // 3) - 2)
  return fuel_mass + calculate_fuel_requirement(fuel_mass)

def day1():
  with open('day1/input.txt', 'r') as module_masses:
    return sum(calculate_fuel_requirement(int(mass)) for mass in module_masses)

if __name__ == '__main__':
  print(day2())
