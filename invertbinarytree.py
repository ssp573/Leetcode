# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return []
        elif root.right or root.left:
            tmp=root.left
            root.left=root.right
            root.right=tmp
            if root.right:
                root.right=self.invertTree(root.right)
            if root.left:
                root.left=self.invertTree(root.left)
        return root
