'''
28. Implement strStr()
Rating: Easy

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Notes:
I can brute force this one easily, but I need to go back and study the rabin-karp solution for this one
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '': return 0
        if len(needle) > len(haystack): return -1

        max_idx = len(haystack) - len(needle) + 1
        j = len(needle)
        for i in range(0, max_idx):
            if haystack[i:j] == needle:
                return i
            j += 1
        return -1


haystack, needle = "hello", "ll"
s = Solution()
print(s.strStr(haystack, needle))