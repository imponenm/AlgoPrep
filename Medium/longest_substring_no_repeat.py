'''
3. Longest Substring Without Repeating Characters
Rating: Medium

Given a string s, find the length of the longest substring without repeating characters

Notes:
Managed to get a solution that runs in O(2n) time with O(min(n, m)) space, where n is the number of unique characters
in s, and m is the number of characters in the alphabet. Sliding window technique.

Turns out I can optimize this to be O(n) time. Good exercise to try this next time
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        n = len(s)
        res, i, j = 0, 0, 0
        subs = set()

        while i < n and j < n:
            if s[j] not in subs:
                subs.add(s[j])
                j += 1
                res = max(res, j - i)
            else:
                subs.remove(s[i])
                i += 1

        return res
