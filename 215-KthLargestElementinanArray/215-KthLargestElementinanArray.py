# Last updated: 12/08/2026 10:58:53
1class Solution(object):
2    def findKthLargest(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        return sorted(nums)[-k]
9        