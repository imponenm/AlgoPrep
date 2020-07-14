'''
819. Most Common Word
Difficulty: Easy

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
It is guaranteed there is at least one word that isn't banned, and that the answer is unique. Words in the list of
banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.
The answer is in lowercase.

Notes:
Complexity os O(N+M), where N is number of characters in the list, and M is number of banned words. Space complexity
is O(N) where N is number of unique words in the input string
'''


from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        h = {}
        cur_word = ""
        for char in paragraph:
            if char.isalpha():
                cur_word = cur_word + char.lower()
            else:
                if cur_word not in banned and cur_word.isalpha():
                    if cur_word in h:
                        h[cur_word] += 1
                    else:
                        h[cur_word] = 1
                cur_word = ""

        if not h:
            return cur_word

        count = 0
        for key in h:
            if h[key] > count:
                count = h[key]
                res = key
        return res