class Solution:
        def numIslands(self, grid: List[List[str]]) -> int:
            COLLS = len(grid[0])
            ROWS = len(grid)
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                                        

            def dfs(r, c):
                if c < 0 or r< 0 or c >= COLLS or r >= ROWS or grid[r][c] == "0":
                    return
                grid[r][c] = "0"

                for direction in directions:
                    c1 = c
                    r1 = r
                    r1 += direction[0]
                    c1 += direction[1]
                    dfs(r1, c1)
                                                                                                                                                                                            
            islands = 0
            for i in range(0, ROWS):
                for j in range(0, COLLS):
                    if grid[i][j] == "1":
                        dfs(i, j)
                        islands += 1
            return islands
                                                                                                                                                                                                                                                                                        

        