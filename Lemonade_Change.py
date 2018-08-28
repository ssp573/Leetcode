class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change={'five':0,'tens':0}
        for item in bills:
            #rint(change)
            if item==5:
                change['five']+=5
            elif item==10:
                if change['five']>=5:
                    change['five']-=5
                    change['tens']+=10
                else:
                    return False
            elif item==20:
                if change['tens']>=10 and change['five']>=5:
                    change['tens']-=10
                    change['five']-=5
                elif change['tens']<10 and change['five']>=15:
                    change['five']-=15
                else:
                    return False
        return True
        
