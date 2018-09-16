class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        answer=[]
        for word in words:
            dir={}
            if len(word) != len(pattern):
                continue
            yes=True
            #print("\n"+word)
            for w,p in zip(word,pattern):
                #print(w,p)
                if w not in dir:
                    if p in dir.values():
                        #print("in")
                        yes=False
                        break
                    dir[w]=p
                else:
                    if dir[w]!=p:
                        yes=False
                        break
            if yes:
                answer.append(word)
        return answer
