class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        stairs=[1 for i in range(n+1)]
        for i in range(2,n+1):
            stairs[i]=stairs[i-1]+stairs[i-2]
        return stairs[n]
