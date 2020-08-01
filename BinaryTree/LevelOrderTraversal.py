'''
Binary tree Level Order Traversal

Runs in O(N) and takes O(N) space
'''

from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        queue = deque([root, ])
        res = []

        while queue:
            tmp = []
            lvl_length = len(queue)

            for i in range(lvl_length):
                cur_node = queue.popleft()
                tmp.append(cur_node.val)

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

            res.append(tmp)

        return res
