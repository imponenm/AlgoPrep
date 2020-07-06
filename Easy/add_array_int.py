'''
989. Add to Array-Form of Integer
Rating: Easy

For a non-negative integer X, the array-form of X is an array of its digits in left to right order.
For example, if X = 1231, then the array form is [1,2,3,1].
Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

Notes:
I think runtime here is O(max(N, log K)). Pretty sleek 3 line solution. Didn't see anything like it on LeetCode
'''
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        a_num = int(''.join(str(x) for x in A))
        total = a_num + K
        return [c for c in str(total)]