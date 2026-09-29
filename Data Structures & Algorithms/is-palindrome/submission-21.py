class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = (''.join([car for car in s if car.isalnum()])).lower()
        
        i, j = 0, len(newS)-1

        while i < j :
            if (newS[i] != newS[j]):
                return False
            else:
                i+=1
                j-=1
        return True