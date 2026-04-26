class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLen = 0;
        for(int i=0; i<s.length(); i++){
            int currLen = 0;
            HashSet<Character> letters = new HashSet<>();
            for(int j=i; j<s.length(); j++){
                if(letters.contains(s.charAt(j))){
                    break;
                }
                currLen++;
                letters.add(s.charAt(j));
            }   
            maxLen = Math.max(currLen, maxLen);
            currLen = 0;
            letters.clear();
        }
        return maxLen;
    }
}
