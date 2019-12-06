#!/usr/bin/env python3
from vm import solve_vm

input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,10,23,1,23,13,27,1,6,27,31,1,9,31,35,2,10,35,39,1,39,6,43,1,6,43,47,2,13,47,51,1,51,6,55,2,6,55,59,2,59,6,63,2,63,13,67,1,5,67,71,2,9,71,75,1,5,75,79,1,5,79,83,1,83,6,87,1,87,6,91,1,91,5,95,2,10,95,99,1,5,99,103,1,10,103,107,1,107,9,111,2,111,10,115,1,115,9,119,1,13,119,123,1,123,9,127,1,5,127,131,2,13,131,135,1,9,135,139,1,2,139,143,1,13,143,0,99,2,0,14,0]

def solve1(memory):
    return solve_vm(input, 12, 2)

def solve2(memory):
    noun = 0
    verb = 0
    while noun < 100:
        noun += 1
        verb = 0
        while verb < 100:
            verb += 1
            if solve_vm(memory, noun, verb) == 19690720:
                return 100 * noun + verb
    raise Exception('Failed to solve')

if __name__ == '__main__':
    # Tests
    assert solve_vm([1,0,0,0,99]) == 2
    assert solve_vm([2,3,0,3,99]) == 2
    assert solve_vm([2,4,4,5,99,0]) == 2
    assert solve_vm([1,1,1,4,99,5,6,0,99]) == 30

    # Part 1
    part1 = solve1(input)
    print("1.", part1)
    assert part1 == 7210630

    # Part 2
    part2 = solve2(input)
    print("2.", part2)
    assert part2 == 3892
