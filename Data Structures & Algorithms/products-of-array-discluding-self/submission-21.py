class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """
        prod = 1
        zcount = 0 # no of 0s decides what happens
        
        for num in nums:
            if num:
                prod *= num
            else:
                zcount += 1

        res = [0] * len(nums)
        if zcount > 1: return res #if any more than one, no matter what, prod is 0

        for i, c in enumerate(nums):
            if zcount:
                res[i] = 0 if c else prod # if one zero, everything except that will be 0
            else:
                res[i] = prod // c # else divide
        return res
        """

        n = len(nums)
        res = [0]*n
        pref = [0]*n
        suff = [0]*n
        
        pref[0] = suff[n-1] = 1

        for i in range(1,n):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(n-2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res