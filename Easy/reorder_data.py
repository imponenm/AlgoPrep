'''
937. Reorder Data in Log Files
Rating: Easy

Notes:
This short piece of code looks simpler than it is.
What we're doing is passing a function to the sorted function that will turn each log entry into a tuple.
If it's a letter log, then the 0th element of the tuple we return is a 0, if it's a digit it's a 1.
Then we put the actual entries as the 1st element in the tuple. The id_ is the last element cause it doesn't matter.
We sort first based on if it's a letter or digit, then we sort based of the entries after that.
The sorted function essentially is converting all these logs into tuples and sorting them, then returns the list
with it's original values, but sorted based off the tuples we created.

Not sure if using the sorted method would fly in an interview or not...
'''


from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
s = Solution()
print(s.reorderLogFiles(logs))