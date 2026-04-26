import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1

        return bisect.bisect_left(nums, target)
        