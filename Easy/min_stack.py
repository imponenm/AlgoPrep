'''
155. Min Stack
Rating: Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Notes:
I did this using a 2 stack approach. Implement a normal stack, but also have a stack to keep track of the minimum
element. Runtime for operations is O(1) since you're only messing with the last element in both lists. Space complexity
is O(N).
Technically space could be improved depending on if there are a lot of duplicate numbers. If that's the case,
a better option would be storing key-value pairs of counts instead of pushing a duplicate value to the min stack
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.minVals = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minVals or x <= self.minVals[-1]:
            self.minVals.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.minVals[-1]:
            del self.minVals[-1]
        del self.stack[-1]   # Note that stack.pop(-1) is an alternative

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVals[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()