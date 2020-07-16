# Implementation of a singly linked list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self, next=None, val=0):
        self.size = 0
        self.head = ListNode()

    def get(self, index: int) -> int:
        if not self.head.next: return -1

        count = 0
        cur = self.head.next
        while cur:
            if count == index:
                return cur.val
            else:
                count += 1
                cur = cur.next
        return -1

    def addAtHead(self, val: int) -> None:
        if not self.head.next:
            self.head.next = ListNode(val)
        else:
            newHead = ListNode(val, self.head.next)
            newHead.next = self.head.next
            self.head.next = newHead
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if not self.head.next:
            self.head.next = ListNode(val)
        else:
            cur = self.head.next
            while cur.next:
                cur = cur.next
            cur.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index > self.size:
            return
        else:
            count = 0
            prev = self.head
            next = prev.next
            while count < index:
                prev = next
                next = next.next
                count += 1
            cur = ListNode(val)
            prev.next = cur
            cur.next = next

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.size == 0:
            return
        elif self.size == 1:
            self.head.next = None
            self.size -= 1
        elif index >= self.size:
            return
        else:
            prev = self.head
            cur = prev.next
            count = 0
            while count < index:
                prev = cur
                cur = cur.next
                count += 1
            if not cur.next:
                prev.next = None
                self.size -= 1
            else:
                prev.next = cur.next



