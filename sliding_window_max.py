class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums)<k or k==0:
            return []
        max_nums=[]
        for i in range(len(nums)-k+1):
            max_nums.append(max(nums[i:i+k]))
        return max_nums
        
