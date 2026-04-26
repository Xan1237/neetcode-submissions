class Solution:
    def climbStairs(self, n: int) -> int:

        cash = [0] * n

        def dfs(i):
            if i >= n:
                return i == n
            if not cash[i]:
                cash[i] = dfs(i + 1) + dfs(i + 2)
            return cash[i]
        return dfs(0)
