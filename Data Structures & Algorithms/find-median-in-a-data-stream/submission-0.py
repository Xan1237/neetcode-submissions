from bisect import bisect_left
class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        idx = bisect_left(self.nums, num)
        self.nums.insert(idx, num) 

    def findMedian(self) -> float:
        mid = len(self.nums) // 2

        if len(self.nums) % 2 == 0:
            return (self.nums[mid-1] + self.nums[mid]) / 2
        else:
            return self.nums[mid]
        
        