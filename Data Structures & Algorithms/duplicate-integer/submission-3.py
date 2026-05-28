class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        letter_set = set(nums)
        return not (len(nums) == len(letter_set))
