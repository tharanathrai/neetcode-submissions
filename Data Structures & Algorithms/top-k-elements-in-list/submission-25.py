class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # need to keep track of how many times something showed up
        # just one pass is enough

        visit = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            visit[num] = 1 + visit.get(num, 0)
        for num, cnt in visit.items():
            freq[cnt].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
            if len(res) == k:
                return res