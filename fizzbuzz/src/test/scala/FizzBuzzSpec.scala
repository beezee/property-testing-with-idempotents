package bz.fizzbuzz

import org.scalacheck.Properties
import org.scalacheck.Prop.{forAll, propBoolean}

object FizzBuzz {
  def apply(nums: List[Int]): List[String] =
    nums.map(n => (n, n % 3, n % 5) match {
      case (0, _, _) => "0"
      case (_, 0, 0) => "FizzBuzz"
      case (_, 0, _) => "Fizz"
      case (_, _, 0) => "Buzz"
      case _ => n.toString
    })
}

object FizzBuzzSpecification extends Properties("FizzBuzz") {

  property("fizzbuzz") = forAll { (nums: List[Int], _seed: Int) =>
    // with isomorphism -> encode(decode(x)) == x
    // with idempotent -> 
    //   inverse(FizzBuzz(inverse(FizzBuzz(nums)))) == 
    //      inverse(FizzBuzz(nums))
    val seed = _seed.max(1).min(Integer.MAX_VALUE / 15)
    val inverse = (_: List[String]).map(x => (x, seed % 5, seed % 3) match {
      case ("0", _, _) => 0
      case ("FizzBuzz", _, _) => 15 * seed
      case ("Buzz", _, 0) => 5 * (seed + 1)
      case ("Buzz", _, _) => 5 * seed
      case ("Fizz", 0, _) => 3 * (seed + 1)
      case ("Fizz", _, _) => 3 * seed
      case (s, _, _) => s.toInt
    })
    ((FizzBuzz(inverse(FizzBuzz(nums))) == FizzBuzz(nums)) :|
      s"${FizzBuzz(inverse(FizzBuzz(nums)))} == ${FizzBuzz(nums)}")
  }

}
