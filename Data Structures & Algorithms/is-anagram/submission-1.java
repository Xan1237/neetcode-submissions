class Solution {
    public boolean isAnagram(String s, String t) {
        ArrayList<Character> letters = new ArrayList<>();
        for(int i=0; i<s.length(); i++){
            letters.add(s.charAt(i));
        }
         for(int i=0; i<t.length(); i++){
            if(letters.contains(t.charAt(i))){
                letters.remove(letters.indexOf(t.charAt(i)));
            }
            else{
                return false;
            }
         }
        if(letters.size() == 0){
            return true;
        }
        return false;
    }
}
