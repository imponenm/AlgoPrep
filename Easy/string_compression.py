'''
443. String Compression
Difficulty: Easy

Given an array of characters, compress it in-place. The length after compression must always be smaller than or equal
to the original array. Every element of the array should be a character (not int) of length 1. After you are done
modifying the input array in-place, return the new length of the array.

Notes:
Used a 2 pointer approach to this one. You have the laggard that stays back in case it needs to write to the list,
while the leader keeps going forward and adds to the count until the next character != the last character.
Runtime is O(N), space complexity O(1)
'''

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return len(chars)

        cur_char = chars[0]
        i, j = 1, 1
        count = 1
        while j < len(chars):
            if cur_char == chars[j]:
                count += 1
                j += 1
            else:
                if count > 1:
                    str_count = str(count)
                    for n in str_count:
                        chars[i] = str(n)
                        i += 1
                cur_char = chars[j]
                chars[i] = cur_char
                i += 1
                j += 1
                count = 1

        if count != 1:
            str_count = str(count)
            for n in str_count:
                chars[i] = str(n)
                i += 1

        chars = chars[:i]
        return len(chars[:i])