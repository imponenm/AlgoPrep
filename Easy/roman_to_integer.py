'''
13. Roman to Integer
Rating: Easy

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Notes:
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
Easiest way to do this is to just include both single and double character symbols.
Since the input is limited, runtime here is O(1) assuming lookups in the table cost O(1)
'''

class Solution:
    def romanToInt(self, s):
        VALUES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                  'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        res, i = 0, 0
        while i < len(s):
            if i < len(s) - 1 and (s[i] + s[i + 1] in VALUES):
                res += VALUES[s[i] + s[i + 1]]
                i += +2
            else:
                res += VALUES[s[i]]
                i += 1
        return res