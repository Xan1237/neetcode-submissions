class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length == 1) return 0;
        int maxPrice = 0;
        int buyPrice = prices[0];
        int sellPrice = prices[1];
        for(int i=0; i<prices.length-1; i++){
            maxPrice = Math.max(maxPrice, (sellPrice-buyPrice));
            if(sellPrice<buyPrice){
                buyPrice = prices[i];
                sellPrice = prices[i+1];
            }
            else{
                sellPrice = prices[i+1];
            }
            maxPrice = Math.max(maxPrice, (sellPrice-buyPrice));
        }
        return maxPrice;
    }
}
