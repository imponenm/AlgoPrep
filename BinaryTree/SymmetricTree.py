'''
Given a binary tree, find if it is symmetric

Recursive, runs in O(N) time and space
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def helper(t1, t2):
            if not t1 and not t2: return True
            if not t1 or not t2: return False

            return ((t1.val == t2.val) and
                    helper(t1.right, t2.left) and
                    helper(t1.left, t2.right))

        return helper(root, root)