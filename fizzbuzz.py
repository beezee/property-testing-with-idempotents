from hypothesis import given
from hypothesis.strategies import lists, integers
from typing import List

def fizzbuzz(nums: List[int]) -> List[str]:
  res: List[str] = []
  for num in nums:
    s = ""
    if num % 3 == 0:
      s += "Fizz"
    if num % 5 == 0:
      s += "Buzz"
    if s == "":
      s = str(num)
    res.append(s)
  return res

@given(lists(integers(), max_size=10), integers(min_value=1))
def test_fizzbuzz(nums: List[int], seed: int) -> None:
  # with isomorphism -> encode(decode(x)) == x
  # with idempotent -> 
  #   inverse(fizzbuzz(inverse(fizzbuzz(x)))) == inverse(fizzbuzz(x))
  def inverse(strs: List[str]) -> List[int]:
    nums: List[int] = []
    for s in strs:
      num = None
      if s == "Fizz":
        num = (seed + 1 if seed % 5 == 0 else seed) * 3
      elif s == "Buzz":
        num = (seed + 1 if seed % 3 == 0 else seed) * 5
      elif s == "FizzBuzz":
        num = seed * 15
      nums.append(num or int(s))
    return nums
  assert inverse(fizzbuzz(inverse(fizzbuzz(nums)))) == inverse(fizzbuzz(nums))
