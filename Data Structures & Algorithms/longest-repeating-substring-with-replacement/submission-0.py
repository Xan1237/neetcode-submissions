class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        amountCharecters = {}
        left = 0
        right = 0
        maxLen = 0
        while right != len(s) and left != len(s):
            amountCharecters.update({s[right] : amountCharecters.get(s[right], 0)+1})
            if max(amountCharecters.values())+k >= right-left+1:
                print("hi")
            else:
                amountCharecters.update({s[left] : amountCharecters.get(s[left], 0)-1})
                left+=1
            right += 1
            maxLen = max(right-left, maxLen)
        return maxLen



        
        