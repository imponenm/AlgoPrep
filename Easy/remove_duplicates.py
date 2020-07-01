'''
26. Remove Duplicates from Sorted Array
Rating: Easy

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Notes:
Pretty simple solution here, just keep track of 2 indices and delete one if their value is the same. Return the length
of the list

Technically this problem only calls for a count to be returned, so you could avoid list removals by just counting
as you go. LeetCode didn't like this for some reason though. It seems like it's checking both values. Oh well
'''


class Solution:
    def removeDuplicates(self, nums):
        if not nums: return 0

        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i + 1]
            else:
                i += 1

        return len(nums)

    def justCount(self, nums):
        if not nums: return 0
        #if len(nums) == 1: return 1

        i, count = 0, 0

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                count += 1
                i = j
        return count + 1
