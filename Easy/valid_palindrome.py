'''
125. Valid Palindrome
Rating: Easy

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
For the purpose of this problem, we define empty string as valid palindrome.

Notes:
Same as regular palindrome check using 2 pointers, but this time we have to check if the characters we are comparing
are alphanumeric before comparing. If it's not, then just move the pointer/s
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "": return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
            elif not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1

        return True
