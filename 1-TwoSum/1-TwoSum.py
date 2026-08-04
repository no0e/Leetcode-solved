# Last updated: 04/08/2026 11:38:23
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dico = {nums[0]:0}
        for i in range(1,len(nums)):
            if target - nums[i] in dico:
                return [dico.get(target - nums[i]),i]
            else: dico[nums[i]] = i
        return None
