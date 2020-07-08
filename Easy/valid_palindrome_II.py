'''
88. Valid Palindrome II
Rating: Easy

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Notes:
Brute force method would be to try deleting every character and running a palindrome check. Instead it's easier
to run an initial check, stop if there's a problem, then run 2 more checks with the strings that start/end with the
character i++ and j--. Runtime is O(N)
'''


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(i, j):
            for k in range(i, j):
                if s[k] != s[j - k + i]:
                    return False
            return True

        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return isPalindrome(i + 1, j) or isPalindrome(i, j - 1)
            i += 1
            j -= 1
        return True