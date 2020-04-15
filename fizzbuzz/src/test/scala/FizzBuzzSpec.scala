package bz.fizzbuzz

import org.scalacheck.Properties
import org.scalacheck.Prop.forAll

object FizzBuzz {
  def apply(nums: List[Int]): List[String] =
    nums.map(n => (n % 3, n % 5) match {
      case (0, 0) => "FizzBuzz"
      case (0, _) => "Fizz"
      case (_, 0) => "Buzz"
      case _ => n.toString
    })
}

object FizzBuzzSpecification extends Properties("FizzBuzz") {

  property("fizzbuzz") = forAll { (nums: List[Int]) =>
    // with isomorphism -> encode(decode(x)) == x
    // with idempotent -> 
    //   inverse(FizzBuzz(inverse(FizzBuzz(nums)))) == 
    //      inverse(FizzBuzz(nums))
    false
  }

}
