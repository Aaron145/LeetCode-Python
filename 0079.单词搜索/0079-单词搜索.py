class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0] or not len(word):
            return False
        
        m, n = len(board), len(board[0])
        if len(word) > m *n:
            return False
        
        self.res = False
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        visited = [[0 for _ in range(n + 1)] for j in range(m + 1)]
        
        def dfs(start, x0, y0):
            if start >= len(word) or board[x0][y0] != word[start]: #�Ҳ�����
                return
            
            visited[x0][y0] = 1
            if board[x0][y0] == word[start]:
                if start == len(word) - 1: #�ҵ�һ�����н���������
                    self.res = True
                    return
                else:
                    for k in range(4):
                        x = x0 + dx[k]
                        y = y0 + dy[k]
                        
                        if 0<= x < m and 0<= y < n and visited[x][y] == 0  and not self.res: #not self.res�ܹؼ�����֦�ǳ���Ҫ
                            dfs(start + 1, x, y) #����һ����ĸ
            visited[x0][y0] = 0 #����
                            
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    dfs(0, i, j) #��ʼ����
                if self.res:
                    return self.res
        return self.res
        
        
        
        