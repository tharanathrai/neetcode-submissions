class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        window = {}

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in window:
                return [window[diff], idx]
            window[val] = idx

'''
    you have an array nums,
    target value to reach
    two indices such that they index numbers that sum the target
    also, there's only one such pair every array
'''

'''
okay so to start with, i and j are indices and not the numbers themselves

target = nums[i] + nums[j]

so if we start with nums[i], it should equal target - nums[j]

or rather, nums[j] should exist where it is target - nums[i]

so just one pass should suffice
'''