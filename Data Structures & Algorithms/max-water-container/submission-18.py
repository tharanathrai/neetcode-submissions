class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # no of slots is abs diff between the indices
        # water amt per slot is min between the two pillars
        # we only care about the max so far, so we can do a greedy check
        # to maximize quantity, the tallest height has to be fixed as one of the bounds

        l = 0
        r = len(heights)-1
        water = 0

        while l < r:
            min_heights = min(heights[l], heights[r])
            width = r - l
            water = max(water, min_heights * width)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return water