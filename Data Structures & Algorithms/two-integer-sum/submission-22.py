class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in visited:
                visited[nums[i]] = i
            else:
                return [visited[diff], i]