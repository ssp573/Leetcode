class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dict_T={}
        not_in=""
        for i in T:
            if i in S:
                if i not in dict_T:
                    dict_T[i]=1
                else:
                    dict_T[i]+=1
            else:
                not_in+=i
        
        answer=""
        for i in S:
            if i in dict_T:
                answer+=i*dict_T[i]
        answer+=not_in
        return answer
        
