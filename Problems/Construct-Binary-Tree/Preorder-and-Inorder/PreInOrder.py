class Solution:
    def buildTree(self, preorder, inorder):
        def recur(preorder, inorder):
            if not preorder: return None
            #current value
            x = preorder[0]
            #split
            i = inorder.index(x)
            inorder_left, inorder_right = inorder[:i], inorder[i+1:]
            preorder_left, preorder_right = preorder[1:i+1], preorder[i+1:]
            #create node
            this = TreeNode(x)
            this.left = recur(preorder_left, inorder_left)
            this.right = recur(preorder_right, inorder_right)
            return this
        
        return recur(preorder, inorder)
