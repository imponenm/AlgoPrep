'''
88. Happy Number
Rating: Easy

Write an algorithm to determine if a number n is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by
the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
Return True if n is a happy number, and False if not.

Notes:
There are several options on how to implement this because of all the different math tricks you could do. Most of the
options are going to be about the same runtime though.

The important thing to understand is that the sum of squares doesn't get THAT big. A cycle actually gets hit pretty
quickly because of this. Easiest to go with a hashmap method
'''


class Solution:

    def sumSquares(self, n: int) -> int:
        total = 0
        while n > 0:
            total += (n % 10) ** 2
            n = n // 10
        return total

    def isHappy(self, n: int) -> bool:
        seen = {}
        res = n

        while res != 1:
            if res in seen:
                return False
            else:
                seen[res] = 1
            res = self.sumSquares(res)

        return True