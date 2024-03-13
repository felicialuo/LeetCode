class Solution:
    def pivotInteger(self, n: int) -> int:
        x = sqrt(n * (n + 1) / 2)
        
        # test if github
        if x % 1 != 0:
            return -1
        else:
            return int(x)