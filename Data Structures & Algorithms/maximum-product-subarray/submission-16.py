class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax = 1
        currMin = 1

        for num in nums:
            temp = num * currMax
            currMax = max(num, temp, num * currMin)
            currMin = min(num, temp, num*currMin)
            res = max(currMax, res)
        return res
            