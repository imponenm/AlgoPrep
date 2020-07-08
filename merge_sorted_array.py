'''
88. Merge Sorted Array
Rating: Easy

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Notes:
You could first merge both list into one, then sort, but that's slow. Second option is 2 pointers and a new list.
This would be O(N) time and space. We could do O(1) space though if we change values in place
'''

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        last_idx = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[last_idx] = nums2[j]
                j -= 1
            else:
                nums1[last_idx] = nums1[i]
                i -= 1
            last_idx -= 1

        # This is for if i reaches below 0 before j does. If that's the case, the remaining values in nums2
        # should all go at the start of nums1, and we've already shifted the higher values to the right.
        # If j reached -1 first, this effectively does nothing
        nums1[:j + 1] = nums2[:j + 1]
