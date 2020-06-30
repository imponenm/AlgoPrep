'''
7. Reverse Integer
Rating: Easy

Given a 32-bit signed integer, reverse digits of an integer.

Notes:
I gotta go back and study this one to understand the optimal solution better. This was tough for being an easy problem.

Signed integer range is [-2^31, 2^31 - 1]. We'll return 0 if the result isn't in this range.

You could do this by converting a python string and using list notation to reverse it, but that's not optimal.
'''

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2 ** 31
        MAX = (2 ** 31) - 1

        # Have to handle positive and negative numbers slightly different
        if x > 0:
            res = int(str(x)[::-1])
        else:
            res = -1 * int(str(-1 * x)[::-1])

        if res not in range(MIN, MAX):
            return 0
        return res