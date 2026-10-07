from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs: #cat
            count = [0]*26
            for c in s: #cat 
                count[ord(c) - ord('a')] += 1 # count = [1, 0, 1, ... 1, ..]
            res[tuple(count)].append(s) # using a tuple since dict keys need to be immutable and lists are mutable 
        return list(res.values())