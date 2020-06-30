'''
9. Palindrome Number
Rating: Easy

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Notes:
There actually is a 1 line solution in python for this: return str(x) == str(x)[::-1]
However, it's not optimal runtime because of the conversions to a string, and list reversal.
Better solution is to pop and push the back half of the input.
'''


class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2 ** 31
        MAX = (2 ** 31) - 1

        mult = 1
        if x < 0:
            x *= -1
            mult = -1

        res = 0
        while x != 0:
            res *= 10
            res += x % 10
            x = x // 10

        res *= mult
        if res not in range(MIN, MAX):
            return 0
        return res