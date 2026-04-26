class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        char[] f = s.toCharArray();
        for(char c : f){
            if(c == '(' || c == '[' || c=='{'){
                System.out.println(c);
                stack.push(c);
            }
            else{
                 if(stack.isEmpty()) return false;
            }
            if(c=='}'){
                if(stack.pop() != '{'){
                    return false;
                }
            }
            if(c==')'){
                if(stack.pop() != '('){
                    return false;
                }
            }
            if(c==']'){
                if(stack.pop() != '['){
                    return false;
                }
            }
        }
        if(stack.isEmpty()){
            return true;
        }
        return false;
    }
}
