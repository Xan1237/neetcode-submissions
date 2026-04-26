class Solution {
    public int maxSubArray(int[] nums) {

        int curr = nums[0];
        int maxSum = nums[0];
        for(int i =1; i<nums.length; i++){
            if(curr<0){
                curr = 0;
            }
            curr += nums[i];
            maxSum = Math.max(curr, maxSum);
        }

        return maxSum;
    }
}
