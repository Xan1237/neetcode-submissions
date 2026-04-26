import math
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #[3,4,5,6,1,2]
        #[1, 2, 3, 4, 5, 6, 7, 8]
        # low, mid, high
        n = len(nums)
        low = 0
        high = n-1
        mid = int(n/2)
        while(low<high):
            mid = int((high+low)/2)
            if nums[mid]<nums[high]:
                high = mid
            else:
                low = mid+1
        return nums[low]




        