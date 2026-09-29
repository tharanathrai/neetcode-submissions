class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = {}
        for num in nums:
            if num not in vals:
                vals[num] = 1
            else:
                return True
        return False
'''
    if nums contains a dupe, return T otherwise F
    
    honestly, using a dictionary here makes sense because i can track the mapping of values and occurrences
'''