'''
283. Move Zeroes
Rating: Easy

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Notes:
2 pointer approach. Runs in O(N) with O(1) space complexity
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 1
        N = len(nums)

        while i < N and j < N:
            x1 = nums[i]
            x2 = nums[j]

            if x1 == 0 and x2 == 0:
                j += 1
            elif x1 == 0 and x2 != 0:
                nums[i] = x2
                nums[j] = 0
            else:
                i += 1
                j += 1
