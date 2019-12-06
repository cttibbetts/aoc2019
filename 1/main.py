import math
fuels = []

with open('input.txt') as file:
  input = file.readlines()

def solve1(masses):
  return sum([calc_fuel(int(mass), False) for mass in masses])
  # return sum([math.floor(int(mass)/3) - 2 for mass in masses])


def solve2(masses):
  return sum([calc_fuel(int(mass)) for mass in masses])

def calc_fuel(mass, consider_fuel=True):
  fuel = math.floor(mass/3) - 2
  if not consider_fuel:
    return fuel
  if fuel < 0:
    return 0
  return fuel + calc_fuel(fuel)

fuels = []
    
with open('input.txt') as file:
  for line in file:
    # mass over three round down minus 2 (recurse)
    fuels.append(calc_fuel(int(line)))

    
if __name__ == '__main__':
  assert calc_fuel(12, False) == 2
  assert calc_fuel(14, False) == 2
  assert calc_fuel(1969, False) == 654
  assert calc_fuel(100756, False) == 33583

  part1 = solve1(input[:])
  print("1.", part1)
  assert part1 == 3479429

  assert calc_fuel(14) == 2
  assert calc_fuel(1969) == 966
  assert calc_fuel(100756) == 50346

  part2 = solve2(input[:])
  print("2.", part2)
  assert part2 == 5216273