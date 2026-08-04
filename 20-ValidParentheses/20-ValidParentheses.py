# Last updated: 04/08/2026 11:38:08
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dico = {
            ")":"(",
            "]":"[",
            "}":"{"
            }
        for c in s:
            if c in ["(","[","{"]:
                stack.append(c)
            else:
                if stack == []:
                    return False
                else:
                    if dico[c] != stack[-1]:
                        return False
                    else:
                        stack.pop()
        return stack == []