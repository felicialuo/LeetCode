class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # always two nums
        num2idx = {}
        for i, num in enumerate(nums):
            if target - num in num2idx:
                return [i, num2idx[target - num]]
            num2idx[num] = i
        return []
            
        