'''
989. Add to Array-Form of Integer
Rating: Easy

Notes:
I think runtime here is O(max(N, log K)). Pretty sleek 3 line solution. Didn't see anything like it on LeetCode
'''
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        a_num = int(''.join(str(x) for x in A))
        total = a_num + K
        return [c for c in str(total)]