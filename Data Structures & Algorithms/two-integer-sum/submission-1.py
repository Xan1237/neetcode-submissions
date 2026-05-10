class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        output = []

        for i in range(len(nums)):
            k = target - nums[i]

            value = targets.get(k, -1)

            if value != -1:
                output.append(value)
                output.append(i)
            targets[nums[i]] = i

        return output