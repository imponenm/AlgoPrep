'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Another problem I've done before. Doesn't hurt doing it again for speed
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1, ptr2 = l1, l2
        tens = 1
        total = 0

        while ptr1 or ptr2:
            x1 = ptr1.val if ptr1 else 0
            x2 = ptr2.val if ptr2 else 0
            total += x1 * tens + x2 * tens
            tens *= 10

            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next

        if total == 0: return ListNode()

        head = ListNode()
        cur = head
        while total:
            cur.next = ListNode(total % 10)
            total //= 10
            cur = cur.next

        return head.next