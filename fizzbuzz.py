from hypothesis import given
from hypothesis.strategies import dictionaries, integers, lists, text
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

@given(
  lists(integers(min_value=1), max_size=10), 
  dictionaries(integers(min_value=1), text())
)
def test_fizzbuzz(nums: List[int], config: Dict[int, str]) -> None:
  # with isomorphism -> encode(decode(x)) == x
  # with idempotent -> 
  #   fizzbuzz(inverse(fizzbuzz(x))) == fizzbuzz(x)
  def make_inverse(
    config: Dict[int, str]
  ) -> Callable[[List[str]], List[int]]:
    def inverse(strs: List[str]) -> List[int]:
      res: List[int] = []
      overrides = list(config.items())
      overrides.sort(key=lambda t: t[0] * -1)
      for s in strs:
        num = None
        for (k, v) in overrides:
          if s == v:
            num = k
            break
        if not num:
          if int(s) % 230 == 0:
            num = -1
        res.append(num or int(s))
      return res
    return inverse
  fizzbuzz = make_fizzbuzz(config)
  inverse = make_inverse(config)
  assert fizzbuzz(inverse(fizzbuzz(nums))) == fizzbuzz(nums)
