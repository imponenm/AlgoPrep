'''
67. Add Binary
Rating: Easy

Given two binary strings, return their sum (also a binary string). The input strings are both non-empty and contains
only characters 1 or 0.

Notes:
The problem didn't specify if I could use str() or not, so I used it. If that wasn't allowed, it's easy enough to
do conditionals on string values, or subtracting ord('0') from each character before adding. Runtime and space will both
be O(N) where N = O(max(len(a), len(b))
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0:
            x1 = int(a[i]) if i >= 0 else 0
            x2 = int(b[j]) if j >= 0 else 0
            local_sum = x1 + x2 + carry

            if local_sum == 0 or local_sum == 1:
                res.append(str(local_sum))
                carry = 0
            elif local_sum == 3:
                res.append('1')
                carry = 1
            else:
                res.append('0')
                carry = 1
            i -= 1
            j -= 1

        if carry != 0:
            res.append(str(carry))

        return ''.join(res[::-1])