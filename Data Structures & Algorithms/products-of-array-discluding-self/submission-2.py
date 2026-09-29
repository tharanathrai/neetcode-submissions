class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * (len(nums))

        prefix=1 #here we just assign values from prefix to the result array first
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix=1 #here, we need to update instead of just assigning as prefix values already in array
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        