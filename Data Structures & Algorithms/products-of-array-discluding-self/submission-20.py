class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        zcount = 0
        
        for num in nums:
            if num:
                prod *= num
            else:
                zcount += 1

        res = [0] * len(nums)
        if zcount > 1: return res

        for i, c in enumerate(nums):
            if zcount:
                res[i] = 0 if c else prod
            else:
                res[i] = prod // c
        return res