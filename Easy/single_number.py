'''
136. Single Number
Difficulty: Easy

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Notes:
This solution wants you to be clever. It's straightforward to use a hashmap for O(N) runtime and space, but there's
a way to do this with O(1) space. Bit manipulation! This is a good problem to review for that. The concept:

a xor 0 = a
a xor a = 0
------------
So let's say a is any given number in our list, and b is the single number. We'd want a way to get b xor 0:

b xor 0 = b
b xor (a xor a) = b

So basically we just xor every element in the list. Associative/distributive property lets us do this
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a ^= num
        return a
