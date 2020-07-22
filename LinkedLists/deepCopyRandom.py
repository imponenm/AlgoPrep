'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the
list or null. Return a deep copy of the list.

Easiest way to do this is using a hashmap, but that takes O(N) space.
An alternative is to interweave the new list we're returning. We are asked to create N new nodes anyways, so this does
not count towards the space requirement. Only extra structures would
'''


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None

        # First we'll iterate making copies without the random pointer
        cur = head
        while cur:
            tmp = cur.next
            cur.next = Node(cur.val)
            cur.next.next = tmp
            cur = cur.next.next

        # Now we can make a second pass, filling in the random pointers and returning a deepcopy
        sentinel = Node(0, head.next, None)
        original = head
        # dup = head.next
        while original:
            dup = original.next
            tmp = original.next.next

            if original.random == None:
                dup.random = None
            else:
                dup.random = original.random.next

            original = tmp
            if original:
                dup.next = original.next

        return sentinel.next


# arr = [[7,None],[13,0],[11,1]]

n1 = Node(7, None, None)
n2 = Node(13)
n3 = Node(11)

n1.next = n2
n2.next = n3

n2.random = n1
n3.random = n2


s = Solution()
s.copyRandomList(n1)