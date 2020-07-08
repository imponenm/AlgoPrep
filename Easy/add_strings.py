'''
415. Add Strings
Rating: Easy

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

Notes:
I'm just gonna do this like old school addition. Worst case it's O(N) where N = MAX(len(num1), len(num2)) + 1.
'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        res = []

        while i >= 0 or j >= 0:
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            tmp_sum = n1 + n2 + carry
            res.append(tmp_sum % 10)
            carry = tmp_sum // 10
            i -= 1
            j -= 1

        if carry != 0:
            res.append(carry)

        return ''.join(str(x) for x in res[::-1])


s = Solution()
print(s.addStrings("9", "1"))