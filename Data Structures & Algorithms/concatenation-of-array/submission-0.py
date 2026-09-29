class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums + nums
        return ans

'''
    array nums, ans
    len n, 2n
    ans[i] = num[i]
    ans[i+n] = num[i]

    return ans
'''