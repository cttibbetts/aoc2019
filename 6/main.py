#!/usr/bin/env python3
testinput = [
  'COM)B',
  'B)C',
  'C)D',
  'D)E',
  'E)F',
  'B)G',
  'G)H',
  'D)I',
  'E)J',
  'J)K',
  'K)L',
]

with open('input.txt') as file:
  input = file.readlines()

def count_hops(planet_list, source, dest):
  source_parents = get_parents(planet_list, source)
  dest_parents = get_parents(planet_list, dest)

  common_parents = set(source_parents) & set(dest_parents)

  source_hops = {}
  for p in common_parents:
    source_hops[p] = count_hops_back_to(planet_list, source, p)

  dest_hops = {}
  for p in common_parents:
    dest_hops[p] = count_hops_back_to(planet_list, dest, p)
  
  return min([source_hops[p] + dest_hops[p] for p in common_parents])


def count_hops_back_to(planet_list, source, dest):
  parent = planet_list.get(source)
  if parent == dest:
    return 0
  return 1 + count_hops_back_to(planet_list, parent, dest)


def get_parents(planet_list, planet):
  parent = planet_list.get(planet)
  if parent is not None:
    return get_parents(planet_list, parent) + [parent]
  return []

def count_orbits(planet_list, planet):
  direct_orbit = planet_list.get(planet)
  if direct_orbit is not None:
    return 1 + count_orbits(planet_list, direct_orbit)
  return 0

def solve1(input):
  planet_list = {}
  for orbit in input:
    inner, outer = orbit.strip().split(')')
    planet_list[outer] = inner
  
  total_count = 0
  for planet in planet_list.keys():
    total_count += count_orbits(planet_list, planet)

  return total_count

def solve2(input):
  planet_list = {}
  for orbit in input:
    inner, outer = orbit.strip().split(')')
    planet_list[outer] = inner
  
  return count_hops(planet_list, 'SAN', 'YOU')

  pass

if __name__ == '__main__':
  # Tests
  assert solve1(testinput[:]) == 42

  # Part 1
  part1 = solve1(input[:])
  print("1.", part1)
  assert part1 == 402879

  # Part 2
  assert solve2(testinput[:] + ['K)YOU', 'I)SAN']) == 4
  part2 = solve2(input[:])
  print("2.", part2)
  assert part2 == 484
