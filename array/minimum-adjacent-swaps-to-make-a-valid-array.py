class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        # find max and min num and ind
        min_num = inf
        max_num = 0

        for i, n in enumerate(nums):
            if n >= max_num: 
                max_num = n
                max_ind = i
            if n < min_num:
                min_num = n
                min_ind = i

        out = len(nums) - 1 - max_ind + min_ind
        if min_ind > max_ind: out -= 1
        return out
