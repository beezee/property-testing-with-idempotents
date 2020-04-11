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

@given(lists(integers(), max_size=10))
def test_fizzbuzz(nums: List[int]) -> None:
  # with isomorphism -> encode(decode(x)) == x
  # with idempotent -> fizzbuzz(inverse(fizzbuzz(x))) == fizzbuzz(x)
  assert False
