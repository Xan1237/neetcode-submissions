class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();

        for(int i : nums){
            set.add(i);
        }

        int longestSequence = 0;
        for (int i=0; i<nums.length; i++){
            int currSequence = 1;
            int j = 1;
            while(set.contains(nums[i]+j)){
                currSequence++;
                j++;
            }
            if(currSequence > longestSequence){
                longestSequence = currSequence;
            }
        }
        return longestSequence;
    }
}
