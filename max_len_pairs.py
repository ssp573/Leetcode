class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort()
        #print(pairs)
        n=len(pairs)
        chain=[1 for i in range(n)]
        for i in range(0,n):
            for j in range(0,i):
                if pairs[i][0]>pairs[j][1] and chain[i]<chain[j]+1:
                    chain[i]=chain[j]+1
        return max(chain)
