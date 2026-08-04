# Last updated: 04/08/2026 12:20:50
1class Solution(object):
2    def findDuplicate(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        slow = nums[0]
8        fast = nums[nums[0]]
9
10        while slow != fast:
11            slow = nums[slow]
12            fast = nums[nums[fast]]
13
14        slow = 0
15        while slow != fast:
16            slow = nums[slow]
17            fast = nums[fast]
18
19        return slow