'''
Remove all elements from a linked list of integers that have value val

I think a clearer way than I did is to use a sentinel node, but I'm effectively doing the same exact thing.
This runs in O(N) time and takes O(1) space
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = None
        cur = head

        while cur:
            if cur.val == val:
                if prev == None:
                    head = head.next
                    cur = head
                else:
                    prev.next = cur.next
                    cur = cur.next
            else:
                prev = cur
                cur = cur.next

        return head