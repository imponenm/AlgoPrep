'''
Max depth of binary tree. Good practice for both top-down and bottom-up

Runs in O(N) and takes O(N) space
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Bottom-up
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return max(leftDepth, rightDepth) + 1
