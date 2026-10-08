class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        make a set using freq count as keys, and numbers as values
        '''
        res = []
        freqs = Counter(nums)

        for ele, count in freqs.most_common(k):
            res.append(ele)

        return res