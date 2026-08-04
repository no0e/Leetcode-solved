# Last updated: 04/08/2026 11:37:19
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        m = 1
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                m = m*nums[i]
            else:
                zero_count += 1
                id_zero = i
                if zero_count >= 2:
                    return [0]*len(nums)
        
        
        if zero_count == 1:
            return [0]*id_zero+[m]+[0]*(len(nums)-id_zero-1)
        else:
            r = []
            for n in nums:
                r.append(m/n)
            return r

        
        return r

        

        

        