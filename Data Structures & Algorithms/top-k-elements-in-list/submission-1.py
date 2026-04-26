class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        values = freq.values()
        keys = freq.keys()

        combined = list(zip(keys, values))
        
        combined.sort(key=lambda x: x[1], reverse=True)
        
        out = []
        for i in range(k):
            out.append(combined[i][0])
        return out
        