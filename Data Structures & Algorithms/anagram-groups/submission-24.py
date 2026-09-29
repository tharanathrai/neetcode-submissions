class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        masterDic = defaultdict(list)

        for val in strs:
            count = [0]*26

            for c in val:
                count[ord(c) - ord("a")] += 1

            masterDic[tuple(count)].append(val)

        return list(masterDic.values())


        # so i had an idea that we had to use character frequencies, but it was vague and i was overwhelming myself with complicated list comparisons
        # that needed to keep track of existence and history in some form. This computed approach is so much better