class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """

        #�� 0, 1, 6, 8, 9 ��ת 180�� �Ժ󣬵õ����µ����� 0, 1, 9, 8, 6 ��
        #2, 3, 4, 5, 7 ��ת 180�� ��,�õ��Ĳ������֡�
        if not num:
            return True
        mapping = {0:0, 1:1, 6:9, 8:8, 9:6}
        invalid = [2,3,4,5,7]
        
        N = int(num)
        n = N
        tmp = 0
        res = list()
        while(n):
            n, tmp = divmod(n, 10)
            if tmp in invalid:
                return False
            res.append(mapping[tmp])
        
        res = res[::-1]
        r = 0
        for i, x in enumerate(res):
            r += 10 ** i * x
        
        return r == N
