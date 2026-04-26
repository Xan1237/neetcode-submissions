class Solution {
    public boolean isPalindrome(String s) {
        s = s.strip();
        int low = 0;
        int high = s.length()-1;
        if(s.length()== 1){
            return true;
        }
        while(low < high){
            while(!Character.isLetterOrDigit(s.charAt(low)) && low < high){
                low++;
            }
            while(!Character.isLetterOrDigit(s.charAt(high)) && low < high){
                high--;
            }
            if(Character.toLowerCase(s.charAt(low)) == Character.toLowerCase(s.charAt(high))){
                low++;
                high--;
            }
            else{
                return false;
            }
        }
        return true;
    }
}
