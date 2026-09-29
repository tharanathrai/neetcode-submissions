class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # need to keep track of how many times something showed up
        # just one pass is enough

        visit = {}
        res = []

        for num in nums:
            if num not in visit:
                visit[num] = 0
            visit[num] += 1

        while k > 0:
            greatestKey = max(visit, key=visit.get)
            res.append(greatestKey)
            visit.pop(greatestKey)
            k -= 1
        
        return res