'''
20. Valid Parentheses
Rating: Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Notes:
I got this one almost immediately, feels like I'm shaking off some rust. Runtime will be O(N)
'''

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []

        left_chars = ['(', '[', '{']
        h = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in left_chars:
                stack.append(char)
            else:
                if not stack:                   # The stack will never be empty here unless the input was invalid
                    return False
                else:                           # Otherwise we'll check to make sure brackets match
                    last_char = stack.pop()
                    if h[last_char] != char:
                        return False

        # If the input had only left brackets, then we never would have popped the stack, so we return false
        if stack:
            return False
        return True