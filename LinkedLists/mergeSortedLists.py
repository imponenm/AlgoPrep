'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

I did this one earlier as an easy problem, but I wrote the code a lot faster this time. It wasn't as elegant, but
it's still an optimal solution
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        sentinel = ListNode()
        cur = sentinel

        while p1 or p2:
            if p1 == None:
                cur.next = p2
                p2 = p2.next
            elif p2 == None:
                cur.next = p1
                p1 = p1.next
            elif p1.val <= p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next

        return sentinel.next
