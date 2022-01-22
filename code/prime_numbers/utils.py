from constants import Constant

def is_valid_input(input):
  return type(input) == int and input >= Constant.FIRST_PRIME