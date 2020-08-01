'''
PreOrder traversal of binary tree

Did this using  a stack
Runtime and space are both O(N). Space on average could be better than O(N) depending on the structure of the tree.
'''

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None

        stack = [root]
        res = []

        while stack:
            curNode = stack.pop()
            res.append(curNode.val)

            if curNode.right:
                stack.append(curNode.right)
            if curNode.left:
                stack.append(curNode.left)

        return res
