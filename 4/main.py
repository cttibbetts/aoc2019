#!/usr/bin/env python3
from collections import Counter

input = [278384, 824795]

def is_increasing(password):
  last = None
  for c in password:
    if last and int(c) < int(last):
      return False
    last = c
  return True

def character_counts(password):
  return Counter(password).values()

def solve1(min, max=None):
  if max is None:
    max = min
  count = 0
  for x in range(min, max+1):
    password = str(x)

    # It is a six-digit number.
    if len(password) != 6:
      continue

    # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    if not is_increasing(password):
      continue
    
    # Two adjacent digits are the same (like 22 in 122345).
    try:
      next(c for c in character_counts(password) if c >= 2)
      count += 1
    except StopIteration:
      pass

  return count

def solve2(min, max=None):
  # Same as part 1
  if max is None:
    max = min
  count = 0
  for x in range(min, max+1):
    password = str(x)

    if len(password) != 6:
      continue

    if not is_increasing(password):
      continue

    # the two adjacent matching digits are not part of a larger group of matching digits.
    if 2 not in character_counts(password):
      continue

    count += 1
  
  return count


if __name__ == '__main__':
  # Part 1
  assert solve1(111111) == 1
  assert solve1(111222) == 1
  assert solve1(223456) == 1
  assert solve1(223450) == 0
  assert solve1(123789) == 0
  part1 = solve1(*input)
  print("1.", part1)
  assert part1 == 921

  # Part 2
  assert solve2(112233) == 1
  assert solve2(123444) == 0
  assert solve2(111122) == 1
  assert solve2(111222) == 0
  assert solve2(123456) == 0
  part2 = solve2(*input)
  print("2.", part2)
  assert part2 == 603
