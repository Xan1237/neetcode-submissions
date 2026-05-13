class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        values = {}

        for i in range(len(numbers)):
            k = target  - numbers[i]

            num = values.get(k, -1)

            if num != -1:
                return [num+1, i+1]
            
            values[numbers[i]] = i
        return -1

