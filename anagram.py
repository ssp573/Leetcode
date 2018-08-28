class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slist=list(s)
        tlist=list(t)
        if sorted(slist)==sorted(tlist):
            return True
        else:
            return False
        
