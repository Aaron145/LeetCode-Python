class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        #ʮ����ת26����
        res = ""
        while(n):
            n-=1
            n, tmp = divmod(n, 26)
            res = chr(ord("A") + tmp) + res
            
        return res