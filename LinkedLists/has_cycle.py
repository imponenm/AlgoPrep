'''
Problem: Has Cycle
Determine if a linked list has a cycle.

Using 2 pointers you can check this. One pointer moves 1 step at a time, the other goes 2 steps. Eventually the faster
pointer will catch up to the slow pointer if there is a cycle. If there isn't, the fast pointer will reach the end
of the list.
Runtime is O(N), or technically O(N+K), where N is the number of nodes in the list, and K is the number of nodes in
the cycle. Space complexity is O(1).
I think I did this one earlier. I got it right away this time without any hints, so that's a good sign.
'''


# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False

        slow = head
        fast = head.next

        while fast.next:
            if slow.val == fast.val:
                return True
            else:
                if fast.next:
                    if fast.next.next:
                        fast = fast.next.next
                        slow = slow.next
                    else:
                        return False
                else:
                    return False
        return False