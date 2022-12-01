class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
          if nums[i] == nums[i + 1]:
            nums[i] = nums[i] * 2
            nums[i + 1] = 0
          
        count = nums.count(0)
        nums = [num for num in nums if num != 0]
        nums.extend([0] * count)
        
        return nums
