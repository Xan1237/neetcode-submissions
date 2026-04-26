class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashSet = set(nums)
        streak = 0
        for num in nums:
            condition = True
            tempStreak = 0
            while condition:
                if num + 1 in hashSet:
                    tempStreak += 1
                    num += 1
                else:
                    condition = False
            streak = max(tempStreak, streak)
        if streak >= 1:
            return streak +1
        return 1