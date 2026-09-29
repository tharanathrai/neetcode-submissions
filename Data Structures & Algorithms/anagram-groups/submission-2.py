class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #we use this to prevent errors when key doesn't exist

        for item in strs:
            count = [0]*26

            for c in item:
                count[ord(c) - ord('a')] += 1 #finding character indices and updating count
            result[tuple(count)].append(item) #keys in dictionary should be immutable, so we convert to tuples
        return list(result.values())
        