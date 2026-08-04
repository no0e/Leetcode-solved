# Last updated: 04/08/2026 11:37:56
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}

        for mot in strs:
            key = tuple(sorted(mot))

            if key not in groups:
                groups[key] = []

            groups[key].append(mot)

        return list(groups.values())