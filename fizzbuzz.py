from hypothesis import given
from hypothesis.strategies import lists, integers
from typing import Callable, Dict, List

def make_fizzbuzz(
  config: Dict[int, str]
) -> Callable[[List[int]], List[str]]:
  overrides = list(config.items())
  overrides.sort(key=lambda t: t[0] * -1)
  def fizzbuzz(nums: List[int]) -> List[str]:
    res: List[str] = []
    for num in nums:
      r = None
      for (k, v) in overrides:
        if num % k == 0:
          r = v
          break
      res.append(r or str(num))
    return res
  return fizzbuzz

@given(lists(integers(), max_size=10), integers(min_value=1))
def test_fizzbuzz(nums: List[int], seed: int) -> None:
  # with isomorphism -> encode(decode(x)) == x
  # with idempotent -> 
  #   fizzbuzz(inverse(fizzbuzz(x))) == fizzbuzz(x)
  def inverse(strs: List[str]) -> List[int]:
    res: List[int] = []
    for s in strs:
      num = None
      if s == "Fizz":
        num = (seed + 1 if seed % 5 == 0 else seed) * 3
      elif s == "Buzz":
        num = (seed + 1 if seed % 3 == 0 else seed) * 5
      elif s == "FizzBuzz":
        num = seed * 15
      res.append(num or int(s))
    return res
  fizzbuzz = make_fizzbuzz({3: "Fizz", 5: "Buzz", 15: "FizzBuzz"})
  assert fizzbuzz(inverse(fizzbuzz(nums))) == fizzbuzz(nums)
