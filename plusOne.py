class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        prev=[]
        print(digits)
        if (digits[-1]==9):
            if len(digits)==1:
                prev=[1]
                digits[-1]=0
            else:
                digits[-1]=0
                prev=self.plusOne( digits[:-1])
            return prev+[digits[-1]]
        else:
            digits[-1]=digits[-1]+1
            return digits
