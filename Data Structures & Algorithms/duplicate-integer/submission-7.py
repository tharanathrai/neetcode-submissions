class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = {}

        for num in nums:
            visited[num] = 1 + visited.get(num, 0)
            if visited[num] > 1:
                return True
        return False