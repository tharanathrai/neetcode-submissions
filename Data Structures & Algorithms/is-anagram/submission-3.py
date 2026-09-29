class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for c in s:
            if c not in countS:
                countS[c] = 1
            else:
                countS[c] = countS[c] + 1
        for c in t:
            if c not in countT:
                countT[c] = 1
            else:
                countT[c] = countT[c] + 1
        return countS == countT

'''
okay let's be real, for two strings to be anagrams, they need to be of the same length first
also, they need to have the same counts of their alphabets, so basically hashmaps?
'''