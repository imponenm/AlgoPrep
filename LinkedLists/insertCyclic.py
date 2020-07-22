'''
Insert into a Cyclic Sorted List
Given a node from a Circular Linked List which is sorted in ascending order, write a function to insert a value
insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single
node in the list, and may not be necessarily the smallest value in the circular list.

Runs in O(N), with O(1) space complexity. Good opportunity to mention test driven development
'''

# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # Handle an empty list
        if not head:
            head.val = insertVal
            head.next = head

        # If there's only 1 item, we can add our value wherever
        if not head.next or head.next == head:
            head.next = Node(insertVal, head)
            return head

        # Otherwise we iterate
        sentinel = Node(None, head)
        cur = head.next
        while cur:
            # Normal insertion
            if insertVal >= cur.val and insertVal < cur.next.val:
                tmp = cur.next
                cur.next = Node(insertVal, tmp)
                break
            # Handle inserting beginning/end of list
            elif cur.val > cur.next.val:
                if insertVal >= cur.val or insertVal <= cur.next.val:
                    tmp = cur.next
                    cur.next = Node(insertVal, tmp)
                    break
            # If we've gone through the entire list, it means the list is uniform. Add the insertValue wherever
            elif cur == head:
                tmp = cur.next
                cur.next = Node(insertVal, tmp)
                break
            cur = cur.next

        return sentinel.next



n3 = Node(3, None)
n2 = Node(3, n3)
n1 = Node(3, n2)
n3.next = n1

s = Solution()
s.insert(n1, 3)

cur = n1
res = []
for i in range(0, 4):
    res.append(cur.val)
    cur = cur.next

print(res)
