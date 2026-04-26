class Solution {
    public int[] productExceptSelf(int[] nums) {
        int totalSum = 1;
        int containsZero = 0;
        int containsZeros = 0;
        for(int i: nums){
            if(i == 0){
                if(containsZero == 1){
                    containsZeros = 1;
                }
                containsZero = 1;
                continue;
            }
            totalSum *=i;
        }
        for(int i=0; i< nums.length; i++){
            if(containsZeros == 1){
                nums[i] = 0;
                continue;
            }
            if(nums[i]==0){
                nums[i] = totalSum;
                continue;
            }
            if(containsZero == 1){
                nums[i] = 0;
                continue;
            }
            nums[i] = totalSum/nums[i];
        }
        return nums;
    }
}  
