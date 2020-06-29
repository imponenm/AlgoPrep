'''
7. Reverse Integer
Rating: Easy

Given a 32-bit signed integer, reverse digits of an integer.

Notes:
Signed integer range is [-2^31, 2^31 - 1]. We'll return 0 if the result isn't in this range.
You could implement a solution by popping and pushing digits, but it's so much simpler and also fast enough
to just cast the int to a string, then reverse that using Python's list notation.
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