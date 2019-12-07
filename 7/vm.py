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
  def __init__(self, memory, inputs=[]):
    self.memory = memory[:]
    self.inputs = inputs
    self.diagnostic = None

  def __iter__(self):
    self.ptr = 0
    self.yielding = False
    return self
  
  def __next__(self):
    operator = self.memory[self.ptr]
    opcode = int(str(operator)[-2:])
    modes = str(operator)[:-2]
    if opcode == 99: # Exit
      raise StopIteration

    if opcode == 1: # Addition
      params = self.get_params(modes, 3)
      noun = self.get_value(*params[0])
      verb = self.get_value(*params[1])
      store = params[2][1]
      self.memory[store] = noun + verb
      self.ptr += 4
    elif opcode == 2: # Multiplication
      params = self.get_params(modes, 3)
      noun = self.get_value(*params[0])
      verb = self.get_value(*params[1])
      store = params[2][1]
      self.memory[store] = noun * verb
      self.ptr += 4
    elif opcode == 3: # write input
      params = self.get_params(modes, 1)
      store = params[0][1]
      self.memory[store] = self.__get_input()
      self.ptr += 2
    elif opcode == 4: # save output
      params = self.get_params(modes, 1)
      output = self.get_value(*params[0])
      self.diagnostic = output
      self.yielding = True
      self.ptr += 2
    elif opcode == 5: # jump if true
      params = self.get_params(modes, 2)
      truthy = self.get_value(*params[0]) != 0
      ptr = self.get_value(*params[1])
      if truthy:
        self.ptr = ptr
      else:
        self.ptr += 3
    elif opcode == 6: # jump if false
      params = self.get_params(modes, 2)
      truthy = self.get_value(*params[0]) != 0
      ptr = self.get_value(*params[1])
      if not truthy:
        self.ptr = ptr
      else:
        self.ptr += 3
    elif opcode == 7: # less than
      params = self.get_params(modes, 3)
      a = self.get_value(*params[0])
      b = self.get_value(*params[1])
      store = params[2][1]
      self.memory[store] = 1 if a < b else 0
      self.ptr += 4
    elif opcode == 8: # equal to
      params = self.get_params(modes, 3)
      a = self.get_value(*params[0])
      b = self.get_value(*params[1])
      store = params[2][1]
      self.memory[store] = 1 if a == b else 0
      self.ptr += 4
    else:
      print('INVALID OP CODE', self.ptr, opcode)
      exit()
  
  def run(self):
    for x in iter(self): 
      if self.yielding:
        self.yielding = False
        yield self.diagnostic

  def get_params(self, modes, length):
    values = self.memory[self.ptr+1:self.ptr+1+length]
    modes = modes.zfill(len(values))
    return [(int(modes[-(i+1)]),v) for i, v in enumerate(values)]
  
  def get_value(self, mode, val):
    return val if mode == 1 else self.memory[val]

  def modify(self, idx, val):
    self.memory[idx] = val
  
  def add_input(self, input):
    self.inputs.append(input)
  
  def __get_input(self):
    return self.inputs.pop(0)
 

  def output(self):
    return self.memory[0]
