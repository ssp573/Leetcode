class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_con=0
        i=0
        count=0
        while i < len(nums):
            if nums[i]==1:
                count+=1
            max_con=max(max_con,count)
            if nums[i]==0:
                count=0
            i+=1
        return max_con
