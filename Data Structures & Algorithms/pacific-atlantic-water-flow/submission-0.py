class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights) 
        COLLS =  len(heights[0]) 
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


        def dfs(r, c, ocean):
            if r < 0 or c < 0 or r >=  ROWS or c >= COLLS:
                return

            if (r,c) in ocean:
                return

            ocean.add((r,c))
            
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLLS and heights[r][c] <= heights[nr][nc]:
                    dfs(nr, nc, ocean)
        
        pacific = set()
        for i in range(0, ROWS):
            dfs(i, 0, pacific)
        for i in range(0, COLLS):
            dfs(0, i, pacific)
        
        adlantic = set()
        for i in range(0, ROWS):
            dfs(i, COLLS-1, adlantic)
        for i in range(0, COLLS):
            dfs(ROWS-1, i, adlantic)

        return [[r,c] for r, c in pacific & adlantic]

        

            
                
             

        