class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        n = len(nums)
        for i in range(n):
            numSet.add(nums[i])
        
        if len(nums) == len(numSet):
            return False
        return True