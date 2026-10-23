class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxV = 0

        '''
            my understanding is that the vol is decided as the number of indices between the tallest and the tallest/second-tallest based on how far apart they are

            from the example, we could have chosen the other 7 height bar IF it was closer to the end of the list

            what if i do a greedy approach? like in a single pass, we keep updating maxV based on whether we choose a pillar or not

            but what is your grounds for deciding what to keep?

            like if 1 was a 6, that would have served as another bar to choose

            what if as we start from left, we can't have the bar height decrease? since, if we're shrinking the width, a shorter height wouldn't help since we want to fit as much water as we can  
        '''

        while l < r:
            # vol is basically diff in indices (r-l) * shorter of the two

            vol = min(heights[l], heights[r]) * (r-l)

            maxV = max(maxV, vol)

            if  heights[l] < heights[r]:
                l +=1
            else:
                r -=1

        return maxV