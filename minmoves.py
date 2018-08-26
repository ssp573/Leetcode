class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        mini=min(nums)
        acc=0
        for i in nums:
            acc+=i-mini
        return acc
        
