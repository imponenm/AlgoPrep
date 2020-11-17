'''
56. Merge Intervals
Rating: Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array
of the non-overlapping intervals that cover all the intervals in the input.
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Notes:

'''

class Solution(object):
    def merge(self, intervals):
        # Sort and then iterate through, keeping track of when a new interval comes into play
        intervals.sort(key=lambda x: x[0])

        ans = []
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans


intervals = [[1,3],[2,6],[8,10],[15,18]]
s = Solution()
print(s.merge(intervals))