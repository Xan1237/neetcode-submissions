# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # This avoids recalculating the idx of a value in the inorder 
        indexes = {val: idx for idx, val in enumerate(inorder)}

        # index in the preorder we are looking at (root)
        self.pre_idx = 0

        def dfs(l, r):

            #base case when there are no elements left in a branch
            if l > r:
                return None
            
            # find the root
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            # find the index of the root in the inorder
            root = TreeNode(root_val)
            mid = indexes[root_val]

            # make recursive calls to both sides of the root to build the sub trees
            root.left = dfs(l, mid-1)
            root.right = dfs(mid + 1, r)
            return root
        
        #we start the range on the whole array before splitting on the root recursivly
        return dfs(0, len(inorder) -1)
        
            
        
        