class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)-1
        end = nums[n]

        for i in range(n, -1, -1):
            distance = end-i
            if nums[i] >= distance:
                end = i
        if end == 0:
            return True
        return False
        