# Last updated: 04/08/2026 11:37:21
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        apparu = set()
        for valeur in nums:
            if valeur in apparu:
                return True
            else:
                apparu.add(valeur)
        return False