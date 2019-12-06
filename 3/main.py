#!/usr/bin/env python3
import math

UP = 'U'
DOWN = 'D'
RIGHT = 'R'
LEFT = 'L'

with open('input.txt') as file:
  input = file.readlines()
  wires = [wire.split(',') for wire in input]

def manhattan(n1, n2):
  return abs(n1) + abs(n2)

def point_name(n1, n2):
  return f"{n1},{n2}"


def getPoints(wire, crosswire=None):
  crosses = []
  wire_points = {}
  x = 0
  y = 0
  hops = 0
  for instruction in wire:
    d = instruction[0]
    length = int(instruction[1:])
    xmod = 0
    ymod = 0
    if d == UP or d == DOWN:
      ymod = -1 if d == UP else 1
    if d == RIGHT or d == LEFT:
      xmod = 1 if d == RIGHT else -1
    for delta in range(0, length):
      hops += 1
      y += ymod
      x += xmod
      spot = point_name(x, y)
      wire_points[spot] = hops
      if crosswire is not None and spot in crosswire:
        crosses.append((x, y))
  return (
    wire_points,
    sorted([manhattan(*cross) for cross in crosses if cross != (0, 0)]),
    sorted([
      wire_points[point_name(*cross)] + crosswire[point_name(*cross)]
      for cross in crosses if cross != (0, 0)
    ])
  )



def solve1(wires):
  wire_points_1, crosses, hops = getPoints(wires[0])
  wire_points_2, crosses, hops = getPoints(wires[1], wire_points_1)
  return crosses[0]

def solve2(wires):
  wire_points_1, crosses, hops = getPoints(wires[0])
  wire_points_2, crosses, hops = getPoints(wires[1], wire_points_1)
  return hops[0]

if __name__ == '__main__':
  # Tests
  assert solve1([
    'R8,U5,L5,D3'.split(','),
    'U7,R6,D4,L4'.split(','),
  ]) == 6
  assert solve1([
    'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','),
    'U62,R66,U55,R34,D71,R55,D58,R83'.split(','),
  ]) == 159
  assert solve1([
    'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(','),
    'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(','),
  ]) == 135

  assert solve2([
    'R8,U5,L5,D3'.split(','),
    'U7,R6,D4,L4'.split(','),
  ]) == 30
  assert solve2([
    'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','),
    'U62,R66,U55,R34,D71,R55,D58,R83'.split(','),
  ]) == 610
  assert solve2([
    'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(','),
    'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(','),
  ]) == 410

  # Part 1
  part1 = solve1(wires)
  print("1.", part1)
  assert part1 == 225

  # Part 2
  part2 = solve2(wires)
  print("2.", part2)
  assert part2 == 35194
