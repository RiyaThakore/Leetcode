class Solution:
    def constructFromPrePost(self, preorder, postorder):
        def recur(preorder, postorder):
            if not preorder: return None
            #current value
            x = preorder[0]
            #split
            preorder_left, preorder_right = [], []
            postorder_left, postorder_right = [], []
            if len(preorder) > 1:
                i, n = preorder.index(postorder[1]), len(preorder)
                preorder_left, preorder_right = preorder[1:i], preorder[i:]
                postorder_left, postorder_right = postorder[n-i+1:], postorder[1:n-i+1] 
            #create node
            this = TreeNode(x)
            this.left = recur(preorder_left, postorder_left)
            this.right = recur(preorder_right, postorder_right)
            return this
        
        return recur(preorder, postorder[::-1])
