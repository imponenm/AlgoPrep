# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None

        res, stack = [], []

        if root.left:
            stack = [root.left]

        while stack:
            curNode = stack.pop()
            res.append(curNode.val)

            if curNode.right:
                stack.append(curNode.right)
            if curNode.left:
                stack.append(curNode.left)

        res.append(root.val)

        if root.right:
            stack = [root.right]

        while stack:
            curNode = stack.pop()
            res.append(curNode.val)

            if curNode.right:
                stack.append(curNode.right)
            if curNode.left:
                stack.append(curNode.left)

        return res


n2 = TreeNode(3, None, None)
n1 = TreeNode(2, n2, None)
root = TreeNode(1, None, n1)

s = Solution()
print(s.inorderTraversal(root))