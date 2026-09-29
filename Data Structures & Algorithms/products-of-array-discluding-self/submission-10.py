class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []

        for i, num in enumerate(nums):

            l, r = 0, len(nums) - 1

            LP = 1
            RP = 1

            while l != i:
                LP = LP * nums[l]
                l += 1

            while r != i:
                RP = RP * nums[r]
                r -= 1

            res.append(LP*RP)
        return res