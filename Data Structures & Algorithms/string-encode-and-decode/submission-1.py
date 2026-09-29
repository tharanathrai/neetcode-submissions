class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s #adding a special delimiter and character count to know the string extent
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s): #overall index for iterating
            j = i #secondary index for finding endpoint of each string
            while s[j] != '#':
                j += 1 #until we hit the delimiter
            length = int(s[i:j]) #extract length from obtained string
            i = j+1 #start of actual string
            j = i+length #end of actual string
            res.append(s[i:j]) #splice into result array
            i = j #bring our iterator to wherever we last stopped

        return res