'''
763. Partition Labels
Rating: Medium

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so
that each letter appears in at most one part, and return a list of integers representing the size of these parts.
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Notes:
This runs in O(N) time, and only takes O(1) space. You just have to get the index of the last occurence for each char,
then keep track of the anchor index, while sliding along the list of chars until you hit a last occurrence
'''

class Solution(object):
    def partitionLabels(self, S):
        # Get the index of the last occurence for each char in S
        last = {c: i for i, c in enumerate(S)}

        # Using anchor and j to keep track of indices
        j = anchor = 0
        ans = []

        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                # Figure out the length and add it to the answer
                ans.append(i - anchor + 1)
                # Move the anchor to the start of the next partition
                anchor = i + 1

        return ans