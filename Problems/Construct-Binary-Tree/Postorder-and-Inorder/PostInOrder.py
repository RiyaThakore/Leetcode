class Solution:
    def buildTree(self, inorder, postorder):
        def recur(inorder, postorder):
            if not postorder: return None
            #current value
            x = postorder.pop()
			#split
            i = inorder.index(x)
            inorder_left, inorder_right = inorder[:i], inorder[i+1:]
            postorder_left, postorder_right = postorder[:i], postorder[i:]
            #create node
            this = TreeNode(x)
            this.left = recur(inorder_left, postorder_left)
            this.right = recur(inorder_right, postorder_right)
            return this
        
        return recur(inorder, postorder)
