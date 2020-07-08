'''
206. Reverse Linked List
Rating: Easy

Reverse a singly linked list.

Notes:
Did this iteratively. It'd be good study practice to try re-writing this recursively
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev