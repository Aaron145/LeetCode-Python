import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        digit = [i for i in range(1, n + 1)] #����1 ~ n���б�
        res = ""
        while n > 0:
            tmp = math.factorial(n - 1) #����һ���ж��������
            idx =  (k - 1) / tmp #��K��tmp��ռ�ı�����ȷ����һλ������
            k -= idx * tmp #��һλȷ��֮��ˢ��k
            res += str(digit[idx])
            digit.pop(idx)
            n -= 1
        return res