class Solution:
    def trap(self, height: List[int]) -> int:
        
        '''
            for trapping water, here are some rules:
                1. the bounding pillars have to be of the same size or at least one more than the other
                2. the right pillar can't be shorter
                3. what if water is just cumulatively calculated and we return the final sum amt
        '''
        water = 0
        l, r = 0, len(height)-1
        lMax, rMax = height[l], height[r]

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                water += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                water += rMax - height[r]

        return water