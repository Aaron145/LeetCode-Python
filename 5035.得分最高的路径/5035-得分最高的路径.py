class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        from heapq import *
        if not A or not A[0]:
            return 0
        
        m, n = len(A), len(A[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        res = 0
        queue = [[-A[0][0], 0, 0]]
        visited = set([0,0])
        heapify(queue)
        while queue:
            val, x0, y0 = heappop(queue) #��Ŀǰ�������ĵ��ҳ���
            if [x0, y0] == [m - 1, n - 1]: #����Ѿ����յ���
                return -val
            
            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]
                
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    visited.add((x, y))
                    heappush(queue, [max(val, -A[x][y]), x, y]) #�ھ����
                    
        
            