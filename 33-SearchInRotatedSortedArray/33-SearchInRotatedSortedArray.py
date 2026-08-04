# Last updated: 04/08/2026 11:38:04
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n-1
        while left <=right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
            else:
                if nums[mid] > target >= nums[left]:
                    right = mid -1
                else:
                    left = mid +1


        return -1
          