class Solution:
    def longestPalindrome(self, s: str) -> str:


        longest = ""
        for j in range (0, len(s)):
            curr = ""
            for i in range (j, len(s)):
                curr += s[i]
                if curr == curr[::-1]:
                    if len(curr) == max(len(longest), len(curr)):
                        longest = curr
        return longest
        