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
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        n = 0
        while x > n:
            n *= 10
            n += x % 10
            if x == n:
                return True
            x = x // 10

        if x == n:
            return True
        return False