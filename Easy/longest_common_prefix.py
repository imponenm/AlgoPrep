'''
14. Longest Common Prefix
Rating: Easy

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ""

Notes:
This one was actually pretty fun. There are a few ways to do this, including divide and conquer and binary search
(both of which I need to practice). Worst case we have n equal strings length m. So runtime for these is generally
O(m*n).

I like a different approach to this though - sort the list first. It'll be in alphabetical order based on prefixes,
so you only have to compare the first and last element in the list. Runtime would be the time it takes to sort,
which is going to be n*log(n) in most cases.

This is slow, but much more concised. I need to come back to this to implement the binary search version of it.
'''

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        strs.sort()
        lcp = ""
        for char1, char2 in zip(strs[0], strs[-1]):
            if char1 == char2:
                lcp += char1
            else:
                return lcp
        return lcp