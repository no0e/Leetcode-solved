# Last updated: 04/08/2026 11:37:02
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        id_debut=0
        id_fin = len(nums) - 1
        while id_fin >= id_debut :
            id_milieu = id_debut + (id_fin-id_debut)//2

            if nums[id_milieu] == target:
                return id_milieu
       
            if target > nums[id_milieu]:
                id_debut = id_milieu +1
            if target < nums[id_milieu]:
                id_fin = id_milieu -1
        return -1
        if target < nums[id_milieu]:
            id_fin = id_milieu
        
        if nums[id_milieu] == target:
            return id_milieu
        else:
            return -1

        