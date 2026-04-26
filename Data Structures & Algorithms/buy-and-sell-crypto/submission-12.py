class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = 0
        r = 1
        l = 0
    
        while r<len(prices):
            if prices[l]<prices[r]:
                currMax = max(currMax, prices[r]-prices[l])
            else:
                l=r
            r+=1
        return currMax


        