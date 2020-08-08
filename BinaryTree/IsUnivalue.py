'''
Given a binary tree, return the count of univalue nodes.
A node is universal if its value is the same as its children's.

Runs in O(N) and takes O(H) space
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root: return 0
        self.count = 0
        self.isUnivalue(root)
        return self.count

    def isUnivalue(self, node):
        # Base case is you're at the bottom
        if not node.left and not node.right:
            self.count += 1
            return True

        isUni = True
        if node.left:
            isUni = self.isUnivalue(node.left) and isUni and node.val == node.left.val
        if node.right:
            isUni = self.isUnivalue(node.right) and isUni and node.val == node.right.val

        if isUni:
            self.count += 1
        return isUni
