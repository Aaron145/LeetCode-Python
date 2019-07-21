class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict, deque
        red_nei, blue_nei = defaultdict(set), defaultdict(set)
        
        for start, end in red_edges: #��¼�����еĴӺ�ɫ·�����Ե�����ھӽڵ�
            red_nei[start].add(end)
        for start, end in blue_edges: #��¼�����еĴ���ɫ·�����Ե�����ھӽڵ�
            blue_nei[start].add(end)
            
        visited = set()
        queue = deque()
        queue.append((0, -1)) # -1 ��ɫ�� 0 ��ɫ�� 1��ɫ
        distance = 0
        res = [-1] * n
        while queue:
            next_queue = deque()
            for cur, color in queue:
                if res[cur] == -1: #BFS�����˵�һ�ε����յ�ʱ�ľ���һ������̾���
                    res[cur] = distance
                if color == -1 or color == 0: #��ǰ�Ǻ�ɫ����һ������ɫ����
                    for nei in blue_nei[cur]:
                        if (cur, nei, 1) not in visited:
                            visited.add((cur, nei, 1))
                            next_queue.append((nei, 1))
                if color == -1 or color == 1: #��ǰ����ɫ����һ���ں�ɫ����
                    for nei in red_nei[cur]:
                        if (cur, nei, 0) not in visited:
                            visited.add((cur, nei, 0))
                            next_queue.append((nei, 0))
            queue = next_queue
            distance += 1
        return res
        