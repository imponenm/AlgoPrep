'''
Binaray Tree In-Order traversal

Recursively this is O(N) space and time, since worst case we visit every node.
This could be done iteravely with a stack as well, and it would give the same space and runtime.

It should be noted that average space can be as good as logN depending on tree structure
'''


# Definition for a binary tree node.
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def helper(root):
            if root:                        # As long as we don't have a null node
                if root.left:               # If there's a left node keep going left
                    helper(root.left)

                res.append(root.val)        # Once we've gone all the way left, add that value to result

                if root.right:              # Now we can move right
                    helper(root.right)

        helper(root)
        return res