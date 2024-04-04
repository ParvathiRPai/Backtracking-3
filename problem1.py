#Time and space complexity is O(N) 
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        res = []
        cols = set()
        posdiag = set()
        negdiag = set()
        
        board = [["."]*n for i in range(n)]
        
        def dfs(r):
            if r==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            
            for c in range(n):
                if c in cols or (r-c) in negdiag or (r+c) in posdiag:
                    continue
                
                cols.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c] = "Q"
                
                dfs(r+1)
                
                cols.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c] = "."
        dfs(0)
        return res
                
                