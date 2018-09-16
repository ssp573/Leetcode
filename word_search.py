class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i,j,board,word):
                    return True
        return False
    
    def dfs(self,i,j,board,word):
        if len(word)==0:
            return True
        if (i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]):
            return False
        temp=board[i][j]
        board[i][j]="#"
        check=self.dfs(i+1,j,board,word[1:]) or self.dfs(i,j+1,board,word[1:]) or self.dfs(i-1,j,board,word[1:]) or self.dfs(i,j-1,board,word[1:])
        board[i][j]=temp
        return check
        
