'''
Binaray Tree PostOrder traversal

Again, I did this recursively and it runs in O(N) space and time.
This was really easy after doing the InOrder traversal. It's literally moving the placement of 1 line of code :D
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def helper(root):
            if root:
                if root.left:
                    helper(root.left)

                if root.right:
                    helper(root.right)

                res.append(root.val)

        helper(root)
        return res
