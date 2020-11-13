'''
238. Product of Array Except Self
Rating: Medium

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product
of all the elements of nums except nums[i].

Notes:
Originally got this done in O(N) space and time, then optimized it for O(1) space after a hint
'''

class Solution(object):
    def productExceptSelf(self, nums):
        # Calculate the product of all elements to the left and right of i
        N = len(nums)

        # First, deal with the left array
        left = [0] * N
        left[0] = 1
        for i in range(1, N):
            left[i] = nums[i - 1] * left[i - 1]

        # Now the right
        right = [0] * N
        right[-1] = 1
        for i in range(N - 1, 0, -1):
            right[i - 1] = nums[i] * right[i]

        # And finally we can get an answer
        ans = [L * R for L, R in zip(left, right)]
        return ans


    def optimized(self, nums):
        # Calculate the product of all elements to the left and right of i
        # Create one of them, let's say the left, while we calculate the other on the fly
        N = len(nums)

        left = [0] * N
        left[0] = 1

        # Setup the left array, which will also serve as our answer
        for i in range(1, N):
            left[i] = nums[i - 1] * left[i - 1]

        # Now do the right on the fly
        R = 1
        for i in reversed(range(N)):
            left[i] = left[i] * R
            R *= nums[i]

        return left