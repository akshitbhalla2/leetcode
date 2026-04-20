# Last updated: 4/19/2026, 11:23:47 PM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        size = len(word)

        starts = []
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    starts.append((r, c))

        path = set()
        def dfs(r, c, i):

            if i == size:
                return True
            
            if (r < 0) or (c < 0) or (r >= m) or (c >= n) or (board[r][c] != word[i]) or ((r, c) in path):
                return False

            path.add((r, c))
            result = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)) 
            path.remove((r, c))   

            return result

        for r, c in starts:
            if dfs(r, c, 0):
                return True

        return False 




        

        

        
        