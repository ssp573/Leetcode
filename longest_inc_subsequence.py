class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums)==1: return 1
        
        lis=[1]*len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    lis[i]=max(lis[i],lis[j]+1)
            
        return max(lis)
