'''
27. Remove Element
Rating: Easy

Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Notes:
Similar to remove duplicates, but this time its just removing a specified value. Again, if we can avoid deletions
that would be great. Since order doesn't matter, we can just use 2 pointers and a count. Runtime is O(N)
'''
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(0, len(nums)):
            if nums[i] != val :
                nums[count] = nums[i]
                count +=1
        return count