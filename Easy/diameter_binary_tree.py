'''
543. Diameter of Binary Tree
Rating: Easy

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the
length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Notes:
From the initial root, check if there is a right and left. If there is, move right and left from each of those nodes
while keeping track of a local and global count. This is essentially a modified depth first search.

Worst case runtime would be O(N), where N is the number of nodes in the tree. This scenario would happen if the tree is
totally balanced. Space complexity is the same, since we're running a recursive call on each node
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 1

        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.res = max(self.res, L + R + 1)
            return max(L, R) + 1

        depth(root)
        return self.res - 1


node5 = TreeNode(5)

node4 = TreeNode(1)
node3 = TreeNode(3, node5)

node2 = TreeNode(2)

node1 = TreeNode(2, node2, node3)
root = TreeNode(4, node1)

s = Solution()
print(s.diameterOfBinaryTree(root))
