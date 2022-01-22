from constants import Constant
from utils import is_valid_input

def is_prime(number):
  if not is_valid_input(number):
    return False
  
  divisor = Constant.FIRST_PRIME
  
  while divisor ** 2 <= number:
    if number % divisor == 0:
      return False
    divisor += Constant.STEP
  
  return True