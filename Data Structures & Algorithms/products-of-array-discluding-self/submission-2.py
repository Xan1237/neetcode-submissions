class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mulNums = [0] * len(nums)

        mulNums[0] = nums[0]
        zeroCount = 0
        zeroIdx = -1
        for i in range(1, len(nums)):
            if nums[i] == 0:
                zeroCount += 1
                zeroIdx = i
                mulNums[i] = mulNums[i-1]
            else:
                mulNums[i] = mulNums[i-1] * nums[i]
        
        if zeroCount > 1:
            return [0] * len(nums)
        if zeroCount == 1:
            arr = [0] * len(nums)
            arr[zeroIdx] = mulNums[len(nums)-1]
            print(mulNums)
            return arr

        print(mulNums)
        for i in range(len(nums)):
            mulNums[i]  = int(mulNums[len(nums)-1] / nums[i])
        return mulNums
        