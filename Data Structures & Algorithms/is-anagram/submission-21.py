class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for num in range(len(s)):
            countS[s[num]] = 1 + countS.get(s[num], 0)
            countT[t[num]] = 1 + countT.get(t[num], 0)

        return countS == countT