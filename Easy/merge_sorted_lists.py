'''
21. Merge Two Sorted Lists
Rating: Easy

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the
nodes of the first two lists.

Notes:
This was a good problem to shake off the rust with linked list. I went ahead and tried both iterative and recursive.
Both wind up with the same runtime of O(n+m), where n and m are the lengths of l1 and l2
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def iterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        # This is essentially a placeholder. We'll return prehead.next, as that's where
        # the linked list will actually start
        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # One of these will have ended the loop because it's null, the other won't be null
        prev.next = l1 or l2

        return prehead.next

    def recursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.alternate(l1.next, l2)
            return l1
        else:
            l2.next = self.alternate(l1, l2.next)
            return l2

'''
origin12 = ListNode(4, None)
origin11 = ListNode(2, origin12)
origin1 = ListNode(1, origin11)

origin22 = ListNode(4, None)
origin21 = ListNode(3, origin22)
origin2 = ListNode(1, origin21)


s = Solution()
res = s.alternate(origin1, origin2)
while res:
    print (str(res.val) + '->', end='')
    res = res.next
'''