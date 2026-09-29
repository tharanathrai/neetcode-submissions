class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #create hashmap to hold values
        freq = [[] for i in range(len(nums) + 1)] #buckets

        #remember we are sorting based on the number of appearances, not numbers themselves 

        for num in nums:
            count[num] = 1 + count.get(num, 0) #build hashmap

        for num, cnt in count.items(): #iterate over hashmap
            freq[cnt].append(num) #populate buckets

        res = []

        for i in range(len(freq) - 1, 0, -1): #iterate backwards
            for num in freq[i]:
                res.append(num)
                if len(res) == k: #stop after k-th item
                    return res
