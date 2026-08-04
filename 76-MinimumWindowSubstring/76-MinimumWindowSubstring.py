# Last updated: 04/08/2026 11:37:52
from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        window = {}
        aim = Counter(t)

        count = 0
        min_len = float("inf")
        left = 0
        res = ""

        for right, char in enumerate(s):

            window[char] = window.get(char, 0) + 1

            if char in aim and window[char] <= aim[char]:
                count += 1

            while count == len(t):

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right+1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in aim and window[left_char] < aim[left_char]:
                    count -= 1

                left += 1

        return res