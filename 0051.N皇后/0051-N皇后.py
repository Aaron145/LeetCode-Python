class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = ["." * n for _ in range(n)]

        res = []
        def checkRowAndCol(row, col):
            for i in range(n):
                if (board[row][i] == "Q" and i != col) or (board[i][col] == "Q" and i != row): #�����˺�����������ͻ
                    return False
            return True
        
        def checkDoubleDio(row, col):
            add = row + col
            sub = col - row
            
            for x in range(n):
                if x == row: #�������������
                    continue
                y = add - x
                # print add,sub, x, y
                if y >= 0 and y < n and x >= 0 and x < n and board[x][y] == "Q": #����/��ͻ
                    return False
            
                y = sub + x
                if y >= 0 and y < n and x >= 0 and x < n and board[x][y] == "Q": #����\��ͻ
                    return False
                
            return True
        
        
        def dfs(row, col):
            if col >= n: #��������λ�ö�������
                return
            board[row] = "." * col + "Q" + (n - col - 1) * "." #�ѻʺ����(row, col)��λ����
            if checkRowAndCol(row, col) and checkDoubleDio(row, col): #���û�з�����ͻ
                if row == n - 1: #������µ������һ���ʺ�
                    # print board
                    res.append(board[:]) #�ҵ�һ�����н���������
                else:
                    for i in range(n): #��Ҫ�Ÿ���Ļʺ�����һ�зŰ�
                        dfs(row + 1, i)
                        
            board[row] = "." * n #���ݣ��ѱ��з��µĻʺ��û���
            # dfs(row, col + 1)
            return

        for i in range(n):
            dfs(0, i)
            
        return res