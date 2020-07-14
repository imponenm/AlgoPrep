'''
387. First Unique Character in a String
Rating: Easy

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Notes:
Just run through the string adding characters to a hashmap, then check the hashmap afterwards.
Runtime is O(N) since hashmap lookup is constant, and space is O(1) since there's a limited set of characters
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = {}
        for i in range(len(s)):
            char = s[i]
            if char in h:
                h[char] = -1
            else:
                h[char] = i

        for key in h:
            if h[key] != -1:
                return h[key]

        return -1