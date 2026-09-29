class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        masterDic = defaultdict(list)

        for val in strs:
            count = [0]*26

            for c in val:
                count[ord(c) - ord("a")] += 1

            masterDic[tuple(count)].append(val)

        return list(masterDic.values())