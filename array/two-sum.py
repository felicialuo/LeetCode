class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []

        # optimized
        num_to_idx = {}
        # for idx, num in enumerate(nums):
        #     num_to_idx[num] = idx
        for i in range(len(nums)):
            num = nums[i]
            if target - num in num_to_idx:
                return [i, num_to_idx[target-num]]
            num_to_idx[num] = i
        return []
                
        