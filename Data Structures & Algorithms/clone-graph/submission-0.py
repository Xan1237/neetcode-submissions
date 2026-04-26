"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        if not node:
            return None
        def dfs(original_node):

            if original_node in old_to_new:
                return old_to_new[original_node]

            copy = Node(original_node.val)

            old_to_new[original_node] = copy

            for neighbor in original_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
            
        return dfs(node)
      