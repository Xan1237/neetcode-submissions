class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        n = len(nums)
        high = n-1
        while low < high:
            mid = int((low + high)/2 )
            if nums[mid]>nums[high]:
                low = mid+1
            else:
                high = mid
        split = low

        response = max(self.binary_search(0, split, target, nums), self.binary_search(split, n-1, target, nums))
        return response


    def binary_search(self,l, r, target, nums):
        while l<r:
            mid = int((l+r)/2)
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid
            else:
                l = mid +1
        if target == nums[l]:
            return l
        return -1



        