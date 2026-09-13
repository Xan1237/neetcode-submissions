class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i >= n:
                return int(i == n)
            elif i  in memo:
                return memo[i]
            else:
                memo[i] = dfs(i+1) + dfs(i+2)
            return memo[i]
        return dfs(0)
        
        
        