class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        res = 0
        
        if not height:
            return 0
        
        l = 0
        r = n-1
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            # We only account for the left max the right is taller
            if height[l] < height[r]:
                l+=1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            # We only account for the right the left is heigher
            else:
                r -=1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res