package bz.fizzbuzz

import org.scalacheck.Properties
import org.scalacheck.Prop.{forAll, propBoolean}

object MakeFizzBuzz {
  def apply[A, B](overrides: List[(A => Boolean, B)], default: A => B)(in: List[A]): List[B] =
    in.map(i => overrides.find(_._1(i)).map(_._2).getOrElse(default(i)))
}

object FizzBuzzSpecification extends Properties("FizzBuzz") {

  property("fizzbuzz") = forAll { 
    (nums: List[Int], _config: List[(Int, String)]) =>
    // with isomorphism -> encode(decode(x)) == x
    // with idempotent -> 
    //   inverse(FizzBuzz(inverse(FizzBuzz(nums)))) == 
    //      inverse(FizzBuzz(nums))
    val config = _config.map(t => (t._1.max(1), t._2))
    val inverse = (_: List[String]).map(s => 
      config.find(_._2 == s).map(_._1).getOrElse(s.toInt))
    val FizzBuzz = MakeFizzBuzz[Int, String](
      config.map(t => ((_: Int) % t._1 == 0, t._2)), _.toString) _
    ((FizzBuzz(inverse(FizzBuzz(nums))) == FizzBuzz(nums)) :|
      s"${FizzBuzz(inverse(FizzBuzz(nums)))} == ${FizzBuzz(nums)}")
  }

}
