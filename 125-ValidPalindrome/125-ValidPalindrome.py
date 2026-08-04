# Last updated: 04/08/2026 11:37:45
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        formated =""
        for char in s:
            if char.isalnum():
                formated += char.lower()
        return formated[::-1] == formated
        
