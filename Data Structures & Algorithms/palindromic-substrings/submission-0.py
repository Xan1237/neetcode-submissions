class Solution:
    def countSubstrings(self, s: str) -> int:
        
        amount = 0
        for j in range (0, len(s)):
            curr = ""
            for i in range (j, len(s)):
                curr += s[i]
                if curr == curr[::-1]:
                    amount += 1
        return amount
        