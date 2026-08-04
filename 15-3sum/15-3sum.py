# Last updated: 04/08/2026 11:38:15
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            g,d = i+1 , n-1
            while g < d:
                somme = nums[i] + nums[g] + nums[d]
                
                if somme < 0:
                    g +=1
                elif somme > 0 :
                    d -=1
                else :
                    result.append([nums[i],nums[g],nums[d]])
                    while g <d and nums[g] == nums[g + 1]:
                        g += 1
                    while g< d and nums[d] == nums[d - 1]:
                        d -= 1
                        
                    g += 1
                    d -= 1

        return result

        