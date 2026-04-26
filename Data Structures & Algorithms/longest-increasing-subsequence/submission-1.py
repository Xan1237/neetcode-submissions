from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        input = [9, 1, 4, 2, 3, 3, 7]
        dp = [1, 1, 1, 1, 1, 1, 1, 1]
        output = 4
        """

        dp = []

        dp.append(nums[0])

        LIS = 1

        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                LIS += 1
                continue

            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]

        return LIS
        