class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(0, n):
            if dp[i] == 0:
                continue
            for word in wordDict:
                j = len(word)
                if s[i:i+j] == word:
                    print(i)
                    dp[j+i] = 1
        if dp[n] == 1:
            return True
        return False
        

