class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        divisor=1
        while x/divisor>=10:
            divisor=divisor*10
        while x!=0:
            leading=x/divisor
            trailing= x%10
            if leading != trailing:
                return False
            else:
                x = (x%divisor)/10
                divisor=divisor/100
        return True

        
        
