'''
Given a binary tree and 2 values, find the lowest common ancestor. All values are unique, and the values
will be present.

Bottom-up recursion runs in O(N) time and space
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def recurseTree(curNode):
            # Base case
            if not curNode: return False

            # Recurse
            left = recurseTree(curNode.left)
            right = recurseTree(curNode.right)

            # Check if the current node is one of the values
            mid = curNode == p or curNode == q

            # If 2 of the flags are true, then we have our answer
            if mid + left + right >= 2:
                self.ans = curNode

            # Otherwise we return true if we've found at least 1 value. Essentially keeping note that we did find 1 val
            return mid or left or right

        recurseTree(root)
        return self.ans
