class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        setS = set(s)
        setT = set(t)
        countS = {}
        countT = {}

        for val in setS:
            countS[val] = 0
        
        for val in setT:
            countT[val] = 0

        for char in s:
            countS[char] += 1

        for char in t:
            countT[char] += 1

        if countS == countT:
            return True
        return False