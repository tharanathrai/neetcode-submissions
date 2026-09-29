class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0: # first num is positive after sorting
                break

            if i > 0 and a == nums[i-1]: #sequential numbers are duplicates
                continue 

            l, r = i + 1, len(nums) - 1 # while keeping an item constant, do 2ptr

            while l < r:
                threeSum = a + nums[l] + nums[r] # did you find your threesome

                if threeSum > 0:
                    r -=1 

                elif threeSum < 0:
                    l += 1

                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1 # reset the next starting L pointer
        return res