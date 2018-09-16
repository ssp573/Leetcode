class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        low=0
        high=len(nums)-1
        return self.createTree(nums,low,high)
    
    def createTree(self,nums,low,high):
        print(low,high)
        if(low<=high):
            nums1=nums[low:high+1]
            root=TreeNode(max(nums1))
            max_ind=nums.index(max(nums1))
            root.left=self.createTree(nums,low,max_ind-1)
            root.right=self.createTree(nums,max_ind+1,high)
            return root
