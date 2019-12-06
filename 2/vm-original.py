#!/usr/bin/env python3

def solve_vm(memory, noun=None, verb=None):
  vm = VM(memory)
  if noun is not None:
    vm.modify(1, noun)
  if verb is not None:
    vm.modify(2, verb)
  for x in iter(vm):
    pass
  return vm.output()

class VM():
  def __init__(self, memory):
    self.memory = memory[:]

  def __iter__(self):
    self.ptr = 0
    return self
  
  def __next__(self):
    op = self.memory[self.ptr]
    if op == 99: # Exit
      raise StopIteration

    noun = self.memory[self.ptr+1]
    verb = self.memory[self.ptr+2]
    out = self.memory[self.ptr+3]

    if op == 1: # Addition
      self.memory[out] = self.memory[noun] + self.memory[verb]
    if op == 2: # Multiplication
      self.memory[out] = self.memory[noun] * self.memory[verb]
    self.ptr += 4

  def modify(self, idx, val):
    self.memory[idx] = val
 

  def output(self):
    return self.memory[0]
