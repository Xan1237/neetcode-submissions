class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            index = hashmap.get(diff, -1)
            if index != -1:
                return [index, i]
            hashmap[nums[i]] = i
        return []
        
