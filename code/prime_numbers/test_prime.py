from prime import is_prime

def test_first_prime():
  assert is_prime(2), "Two is a prime number"

def test_negative_integers():
  assert not is_prime(-1), "Integers must be positive"

def test_invalid_input():
  invalid_input = [
    "Rony",
    {
      "Hola": "Mundo",
      "Adios": 0.43,
    },
    [
      1,
      "Hancco",
      -6.9,
    ],
  ]
  for input in invalid_input:
    assert not is_prime(input), "Input must be a positive integer"

def test_prime_numbers():
  prime_numbers = [
    20333,
    61381,
    503,
    1693,
    71237,
    33203,
    86729,
    50131,
    40529,
    27581,
    57751,
    4339,
    15493,
    11059,
    97841,
    26987,
    67651,
    81307,
    24061,
    49783,
  ]
  for prime_number in prime_numbers:
    assert is_prime(prime_number), "{number} is a prime number".format(number=prime_number)