class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        window = {}

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in window:
                return[window[diff],idx]
            window[val] = idx