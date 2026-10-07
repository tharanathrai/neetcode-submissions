class Solution:

    def encode(self, strs: List[str]) -> str:
        resString = ''

        for s in strs:
            resString += str(len(s)) + '#' + s
        return resString

    def decode(self, s: str) -> List[str]:
        # s is 3#top3#cat

        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            # i=0, j=1

            wordlength = int(s[i:j]) # wordlength = 3
            i = j+1 # i=2
            j = wordlength + i #j=5
            res.append(s[i:j])
            i = j
        return res