class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i, nums in enumerate(nums):
            x = target-nums
            if x in lookup:
                return[lookup[x],i]
            lookup[nums]=i    
        