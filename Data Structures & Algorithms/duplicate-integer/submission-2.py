class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNums = set()
        for i in range(len(nums)):
            setNums.add(nums[i])
        if len(setNums) == len(nums):
            return False
        return True