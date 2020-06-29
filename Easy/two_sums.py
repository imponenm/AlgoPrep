'''
1. Two Sums
Rating: Easy

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Ex) Given nums = [2, 7, 11, 15], target = 9
    Return [0,1]

Notes:
Create a hashtable to solve this efficiently. We're basically just reversing the list for an easy lookup.
If we subtract the target from the current num, and the result of that number is a key in the hashtable,
then we know that's the complement.
'''

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        table = {}

        for i, num in enumerate(nums):
            n = target - num
            if n not in table:
                table[num] = i
            else:
                return [table[n], i]