class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2*n)
        for i, val in enumerate(nums):
            ans[i] = ans[i+n] = val
        return ans


'''
    array nums, ans
    len n, 2n
    ans[i] = num[i]
    ans[i+n] = num[i]

    return ans

    we know from the question that it is the concat of 2 nums arrays, so it's twice the size
'''

# return ans = (nums + nums) works but you did basic concat operation, so it is not allowed
# doing ans = nums and then iterating works but you're not building it at a low-level
