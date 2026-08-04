# Last updated: 04/08/2026 11:37:43
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)))
        m=1
        curr_m = 1
        n= len(nums)
        if n == 0:
            return 0
        else:
            for i in range(1,n):
                if nums[i] == nums[i-1]+1:
                    curr_m +=1
                    if curr_m > m:
                        m = curr_m
                else:
                    curr_m = 1
            return m


                

            
