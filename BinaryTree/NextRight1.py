'''
You are given a *perfect binary tree* where all leaves are on the same level, and every parent has two children.
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should
be set to NULL

I got this one right away without help which feels good. However I wrote it to run in O(N) time and space.
There's a better solution that takes constant space. I'll come back to this later when I review
'''


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root

        q, children, res = deque([root]), [], []

        while q:
            # Pop the next node in the queue and take note of it's children
            curNode = q.popleft()
            if curNode.left:
                children.append(curNode.left)
            if curNode.right:
                children.append(curNode.right)

            # If we still have nodes in the queue, we can set the next pointer of the current node
            if q:
                curNode.next = q[0]
            # Otherwise add the next level to the q, and reset the temp children list
            else:
                q.extend(children)
                children = []

        return root