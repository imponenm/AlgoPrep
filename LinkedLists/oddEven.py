'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking
about the node number and not the value in the nodes.

Runs in O(N) time with O(1) space. Make 2 separate lists then combine
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        count = 1
        listA, listB = ListNode(), ListNode()
        endA, endB = listA, listB
        cur = head

        while cur:
            if count % 2 == 1:
                endA.next = cur
                endA = endA.next
            else:
                endB.next = cur
                endB = endB.next
            count += 1
            cur = cur.next

        endA.next = listB.next
        endB.next = None

        return listA.next