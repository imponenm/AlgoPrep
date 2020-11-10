'''
91. Decode Ways
Rating: Medium

A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Notes:
Did this recursively for O(N) time and space. You could do this dynamically too, which could be optimized to be O(1) space
'''


class Solution(object):
    # Initialize with a list to store visited indices so we don't backtrack
    def __init__(self):
        self.memo = {}

    def recurse(self, index, s):
        # If we're on the last character add 1
        if index == len(s):
            return 1

        # If we see a 0, that can't be decoded
        if s[index] == '0':
            return 0

        # If we hit the end and it's not 0, add 1
        if index == len(s) - 1:
            return 1

        # Check to make sure we haven't already visited the index
        if index in self.memo:
            return self.memo[index]

        # Otherwise, we can make a recursive call
        res = self.recurse(index + 1, s) + (self.recurse(index + 2, s) if (int(s[index:index + 2]) <= 26) else 0)

        # Save current index
        self.memo[index] = res

        return res

    def numDecodings(self, s):
        if not s:
            return 0
        return self.recurse(0, s)