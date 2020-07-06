'''
53. Maximum Subarray
Rating: Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Notes:
Divide and conquer would be O(N*logN), but we could use a greedy algorithm on this one to get O(N).
In an interview, it would be good to draw out the matrix of indices and how the current and global sums change at
each index.
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum = cur_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], nums[i] + cur_sum)
            global_sum = max(cur_sum, global_sum)
        return global_sum