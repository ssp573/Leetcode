class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        l=len(cost)
        ans=[0]*(l+1)
        for i in range(2,l+1):
            ans[i]=min((ans[i-1]+cost[i-1]),(ans[i-2]+cost[i-2]))
        return ans[l]
        
        
        
        
