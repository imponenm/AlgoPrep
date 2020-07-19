'''
Given a linked list, return True if it is a palindrome, else False

One way to do this is with 2 pass, where you iterate through the LL once, adding the values to an array. You then
use the standard 2 pointer palindrome check for O(N) time and space.

A more elegant way is with recursion. I need to practice this. It's also using O(N) time and space though

A 3rd way that would use O(1) space is by modifying the array in place. This isn't one pass, but it's still O(N) and
uses constant space. Steps for this would be:
1. Find the halfway point in the list (using 2 runners technique)
2. Reverse the back half of the list
3. Check if list is a palindrome
4. Restore the list
5. Return the results
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(self, head: ListNode) -> bool:

    self.front_pointer = head

    def recursively_check(current_node=head):
        if current_node is not None:
            if not recursively_check(current_node.next):
                return False
            if self.front_pointer.val != current_node.val:
                return False
            self.front_pointer = self.front_pointer.next
        return True

    return recursively_check()