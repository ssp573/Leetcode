class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        lps=[[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            lps[i][i]=1
        
        for sublen in range(2,len(s)+1):
            for i in range(0, len(lps)-sublen+1):
                j=i+sublen-1
                if sublen==2 and s[i]==s[j]:
                    lps[i][j]=2
                elif s[i]==s[j]:
                    lps[i][j]=2+lps[i+1][j-1]
                else:
                    lps[i][j]=max(lps[i+1][j],lps[i][j-1])
                    
        
        return lps[0][len(s)-1]
