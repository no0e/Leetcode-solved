# Last updated: 04/08/2026 11:38:18
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n= len(s)
        max_lenght = 0
        curr = set()
        g,d = 0,0
        while d<n:
            if s[d] in curr:
                while s[d] in curr:
                    curr.remove(s[g])
                    g+=1
                
            else:
                while d<n and s[d] not in curr:
                    curr.add(s[d])
                    d+=1

            max_lenght = max(max_lenght,d-g)
        return max_lenght


