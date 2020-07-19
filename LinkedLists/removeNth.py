'''
Given a linked list, remove the n-th node from the end of list and return its head.

This can be done in a single pass by using 2 pointers. Set the laggard to be at the head, and have the leader
be place n-1 nodes away from it. Step through the LL until the leader reaches the end. The laggard pointer will now
be on the node that needs to be removed
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # If the length is 1 we just return an empy list
        if head.next == None: return None

        # Let's set the leader node
        laggard = head
        leader = head
        count = 0
        while count < (n - 1):
            leader = leader.next
            count += 1

        # We need an exception for if the list is length 2
        if leader.next == None:
            return laggard.next

        # Now let's step together until leader hits the end
        while leader.next != None:
            if leader.next.next == None:
                prev = laggard
            leader = leader.next
            laggard = laggard.next

        # Now we can replace the node
        tmp = prev.next.next
        prev.next = tmp

        return head
