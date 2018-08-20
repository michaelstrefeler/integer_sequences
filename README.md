# integer_sequences

>A python project used to demonstrate different number sequences

## DISCLAIMER

I do not own any of the images used in this README file

## Fibonacci number / sequence

F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1

The Fibonacci sequence is a well known sequence of numbers.
To get the next number of the sequence you just have to add the last two numbers together.

![Golden Spiral](https://i.imgur.com/zg7ljPn.png "Golden Spiral")

[Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number)

[Fibonacci OEIS](https://oeis.org/A000045)

## Padovan sequence

a(n) = a(n-2) + a(n-3) with a(0)=1, a(1)=a(2)=0

The Padovan sequence is named after Richard Padovan.
To get the next number you need to add the number 2 back and the number 3 back together.
For example if you have 1, 0, 0, 1, 0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9 to get the next number you need to add 5 and 7 together which will give you 12.

Here's a spiral of equilateral triangles with side lengths which follow the Padovan sequence.
![Padovan triangle](https://i.imgur.com/4wFDZ0Y.png "Padovan triangle")

[Padovan sequence](https://en.wikipedia.org/wiki/Padovan_sequence)

[Padovan OEIS](https://oeis.org/A000931)

## Jacobsthal number

a(n) = a(n-1) + 2*a(n-2), with a(0) = 0, a(1) = 1

In mathematics, the Jacobsthal numbers are an integer sequence named after the German mathematician Ernst Jacobsthal. This sequence is related to the Fibonacci sequence, but instead of adding the last two numbers you have to add the last number twice to the number before that.

For example if you have 0, 1, 1 to get the bext number you do 2 * 1 + 1 = 3

[Jacobsthal number](https://en.wikipedia.org/wiki/Jacobsthal_number)

[Jacobsthal number OEIS](https://oeis.org/A001045)

## Pell number

a(0) = 0, a(1) = 1; for n > 1, a(n) = 2*a(n-1) + a(n-2)

In mathematics, the Pell numbers are an infinite sequence of integers, known since ancient times, that comprise the denominators of the closest rational approximations to the square root of 2.

The sides of the squares used to construct a [silver spiral](https://en.wikipedia.org/wiki/Silver_ratio) are the Pell numbers
![Silver Spiral](https://i.imgur.com/PbR5ZqD.png "Silver spiral approximation")

[Pell Number](https://en.wikipedia.org/wiki/Pell_number)

[Pell Number OEIS](https://oeis.org/A000129)

## Tribonacci numbers

a(n) = a(n-1) + a(n-2) + a(n-3) with a(0)=a(1)=0, a(2)=1

The tribonacci numbers are like the Fibonacci numbers, but instead of adding the last two numbers, you add the last 3 numbers

Here are the first few numbers of the sequence : 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927

[Tribonacci sequence](https://en.wikipedia.org/wiki/Generalizations_of_Fibonacci_numbers#Tribonacci_numbers)

[Tribonacci OEIS](https://oeis.org/A000073)

## Tetranacci numbers

The tetranacci numbers are like the tribonacci numbers, but you add the last 4 numbers instead.

Here are the first few numbers of the sequence: 0, 0, 0, 1, 1, 2, 4, 8, 15, 29, 56, 108, 208, 401, 773, 1490, 2872, 5536, 10671

[Tetranacci numbers](https://en.wikipedia.org/wiki/Generalizations_of_Fibonacci_numbers#Tetranacci_numbers)

[Tetranacci OEIS](https://oeis.org/A000078)