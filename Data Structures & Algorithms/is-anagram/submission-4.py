class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

'''
okay let's be real, for two strings to be anagrams, they need to be of the same length first
also, they need to have the same counts of their alphabets, so basically hashmaps?
'''

'''
solution:
    the character comparison section can be better significantly cut down

    currently, you're if-else for every character and appending values for the count
    you can use get(c,0) for every character to get the count safely
'''