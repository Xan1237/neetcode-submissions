class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:   
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
        

        VISITING, VISITED, UNVISITED = 0, 1, 2
        
        state = [UNVISITED] * numCourses
        
        def dfs(node):

            if state[node] == VISITING:
                return False
            if state[node] == VISITED:
                return True
        
            state[node] = VISITING

            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            state[node] = VISITED
            return True
        
        return all(dfs(i) for i in range(numCourses))