class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # Tracks connections and indegree
        adj = {c: set() for w in words for c in w}
        indegree = {c : 0 for c in adj}

        # add connections to first word and increase indegree of w2
        for  i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        # for all base nodes in the graph (indegree 0)
        q = deque([c for c in indegree if indegree[c]==0])
        res = []

        # Decrease neighbors indegree as we add to results array
        while q:
            char = q.popleft()
            res.append(char)
            for neighbor in adj[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # All the nodes in the graph where not added error
        if len(res) != len(indegree):
            return ""
        
        # Convert the array to the desired string output
        return "".join(res)