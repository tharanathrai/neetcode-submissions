class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        need to find k most frequent elements, i can create a hashmap of frequencies for every item+
        '''

        count = {}
        freaks = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freaks[c].append(n)

        res = []

        for i in range(len(freaks) - 1, 0, -1):
            for num in freaks[i]:
                res.append(num)
                if len(res) == k:
                    return res