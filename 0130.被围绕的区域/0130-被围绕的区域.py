class UnionFindSet(object):
    def __init__(self, grid):

        m, n = len(grid), len(grid[0])
        self.roots = [i for i in range(m * n)]
        self.rank = [0 for i in range(m * n)]
        self.count = n
        
        for i in range(m):
            for j in range(n):
                self.roots[i *n + j] = i * n +j

    def find(self, member):
        tmp = []
        while member != self.roots[member]:
            tmp.append(member)
            member = self.roots[member]
        for root in tmp:
            self.roots[root] = member
        return member
        
    def union(self, p, q):
        parentP = self.find(p)
        parentQ = self.find(q)
        if parentP != parentQ:
            if self.rank[parentP] > self.rank[parentQ]:
                self.roots[parentQ] = parentP
            elif self.rank[parentP] < self.rank[parentQ]:
                self.roots[parentP] = parentQ
            else:
                self.roots[parentQ] = parentP
                self.rank[parentP] -= 1
            self.count -= 1

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        if not board or not board[0]:
            return board
        
        m, n = len(board), len(board[0])

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        def dfs(x, y):
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
 
                if xx >= 0 and xx < m and yy >= 0 and yy < n: #��ǰ������Ч
                    if board[xx][yy] == "O":
                        board[xx][yy] = "P" #���߹��ĵ�Ⱦɫ
                        dfs(xx, yy)
        #--------�����ڴ��������������ڵ����е�
        i = 0
        for j in range(n): #�ϱ�
            if board[i][j] == "O":
                board[i][j] = "P"
                dfs(i, j)
 
        i = m - 1
        for j in range(n): #�±�
            if board[i][j] == "O":
                board[i][j] = "P"
                dfs(i, j)    
        j = 0        
        for i in range(m): #���
            if board[i][j] == "O":
                board[i][j] = "P"
                dfs(i, j) 
 
        j = n - 1     
        for i in range(m): #�ұ�
            if board[i][j] == "O":
                board[i][j] = "P"
                dfs(i, j) 
        #--------�����ڴ��������������ڵ����е�
        # print board
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "P": #ͳ��һ�»��ж��ٸ�û��ȥ���ĵ�
                    
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
                        
        return board
                        
                     