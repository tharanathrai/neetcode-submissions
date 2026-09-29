class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans


'''
    array nums, ans
    len n, 2n
    ans[i] = num[i]
    ans[i+n] = num[i]

    return ans
'''

# return ans = (nums + nums) works but you did basic concat operation, so it is not allowed