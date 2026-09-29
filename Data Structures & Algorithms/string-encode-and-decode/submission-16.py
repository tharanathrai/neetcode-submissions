class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for val in strs:
            res += str(len(val)) + '#' + val
        return res

    def decode(self, s: str) -> List[str]:
        outList = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j+1 # exclude the length indicator
            j = i+length # get characters after delimiter
            outList.append(s[i:j])
            i = j
        return outList
