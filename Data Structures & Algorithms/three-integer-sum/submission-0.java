class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> list = new HashSet<>();

        for(int i=0; i<nums.length; i++){
            HashSet<Integer> seen = new HashSet<>();
            for(int j=i+1; j<nums.length; j++){
                int target = -(nums[i]+nums[j]);
                if(seen.contains(target)){
                   List<Integer> trip = Arrays.asList(nums[i], nums[j], target);
                   Collections.sort(trip);
                   list.add(trip);
                }
                seen.add(nums[j]);
            }
        }
        return new ArrayList<>(list);
    }
}
