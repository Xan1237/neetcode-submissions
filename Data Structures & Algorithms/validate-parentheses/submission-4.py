from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        # queue with paren
        # if its a closing we pop it

        paren = deque()

        for char in s:
            print(paren)
            if char in "({[":
                paren.append(char)
            elif len(paren) == 0:
                return False
            elif char == ")":
                if paren.pop() != "(":
                    return False
            elif char == "}":
                if paren.pop() != "{":
                    return False
            elif char == "]":
                if paren.pop() != "[":
                    return False
        if len(paren) == 0:
            return True
        return False    
        
            
