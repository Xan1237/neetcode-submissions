class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mostWater = 0
        n = len(heights)
        l = 0
        r = n-1

        while l != r:
            water = min(heights[l], heights[r]) * (r-l)
            mostWater = max(mostWater, water)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return mostWater