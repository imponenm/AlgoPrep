'''
Given 2 linked lists, return the node that they intersect at. Return None if they do not intersect

Runtime is O(N), space complexity O(1). The trick here is the 2 pointer approach.
Iterate through list A and B at the same time. If you reach the end of list A, set the pointer to the head of listB,
then continue stepping. Vice versa. If there is an intersection the pointers are guaranteed to intersect. You know
there's no intersection if you reach the end of a list for the 3rd time
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        if headA == headB: return headA
        if not headA.next and not headB.next: return None

        # Set pointers and a count to know when we hit the end of a list.
        # If we hit an end 3 times there's no intersection
        ptr1, ptr2 = headA, headB
        endCount = 0

        # First iteration
        while endCount < 3:
            # Move the pointers
            ptr1 = ptr1.next
            ptr2 = ptr2.next

            # Adjust if we reach the end of the list and increment the count
            if ptr1 is None:
                ptr1 = headB
                endCount += 1
            if ptr2 is None:
                ptr2 = headA
                endCount += 1

            # Return the node if it intersects
            if ptr1 == ptr2:
                return ptr1

        return None