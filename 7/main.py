#!/usr/bin/env python3
from vm import VM

input = [3,8,1001,8,10,8,105,1,0,0,21,38,55,72,93,118,199,280,361,442,99999,3,9,1001,9,2,9,1002,9,5,9,101,4,9,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,1002,9,4,9,4,9,99,3,9,101,4,9,9,1002,9,3,9,1001,9,4,9,4,9,99,3,9,1002,9,4,9,1001,9,4,9,102,5,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,3,9,102,5,9,9,101,4,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99]

# Python function to print permutations of a given list 
def permutation(lst): 
  
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = lst[:i] + lst[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 
  

def try_amps(memory, input):
  amps = ['A', 'B', 'C', 'D', 'E']
  if len(input) != len(amps):
    print('INPUT LENGTH IS WRONG')
  signal = 0
  for idx, amp in enumerate(amps):
    vm = VM(memory, [input[idx], signal])
    for diagnostic in vm.run():
      signal = diagnostic
    pass
  return signal

def try_amps_forever(memory, input):
  amps = [ VM(memory, [phase]) for phase in input ]
  runners = [ amp.run() for amp in amps ]
  signal = 0

  idx = 0
  while idx < len(amps):
    amps[idx].add_input(signal)
    try:
      signal = next(runners[idx])
    except StopIteration:
      break
    idx += 1
    if idx == len(amps):
      idx = 0

  return signal
    
def solve1(memory):
  phases = [0,1,2,3,4]
  all_inputs = permutation(phases)
  values = [(input, try_amps(memory[:], input)) for input in all_inputs]
  best_value = (None, 0)
  for value in values:
    if value[1] > best_value[1]:
      best_value = value
  return best_value[1]
  

def solve2(memory, force_phase=None):
  phases = [5,6,7,8,9]
  all_inputs = [force_phase] if force_phase is not None else permutation(phases)
  values = [(input, try_amps_forever(memory[:], input)) for input in all_inputs]
  best_value = (None, 0)
  for value in values:
    if value[1] > best_value[1]:
      best_value = value
  return best_value[1]

if __name__ == '__main__':
  # Tests
  assert solve1(
    [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0],
  ) == 43210

  # Part 1
  part1 = solve1(input[:])
  print("1.", part1)
  # assert part1 ==

  # Part 2
  assert solve2(
    [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
  ) == 139629729
  part2 = solve2(input)
  print("2.", part2)
  # assert part2 == 

1. 368584
2. 35993240
