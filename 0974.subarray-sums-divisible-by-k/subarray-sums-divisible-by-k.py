class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        s = [0 for i in range(len(A) + 1)] #s����ǰ׺�ͣ���s[i]��ʾsum(A[:i])
        kcnt = [0 for i in range(K)] #k[i]����s���ж��ٸ�Ԫ�� mod k Ϊi
        for i in range(len(A)):
            s[i + 1] = s[i] + A[i]
        for item in s:
            kcnt[item % K] += 1
        print s, kcnt
        #��Ŀ������������ĺ��ܱ�K����������������ĺ;Ϳ��Ա�ʾΪǰ׺�͵Ĳ�
        #���� sum(A[i:j + 1]) = s[j + 1] - s[i]
        #����������Ĳ��ܱ�K��������˵���������� mod k�õ��Ľ����ͬ
        #ֻҪ���ж��ٶ� mod k ��ͬ�����Ϳ��Եõ����
        #���� ����[4,5,0,-2,-3,1] 5
        # s = [0, 4, 9, 9, 7, 4, 5] 
        # k = [2, 0, 1, 0, 4] ������s��������Ԫ�ص�������Ϊ0����0��5����1��Ԫ�ص�����Ϊ2����7�����ĸ�Ԫ�ص�����Ϊ4����4994��
        # �����ڱ�֤������ͬ������£�ȡ�������������Եõ�һ��𰸡�����������Ӵ𰸾��� C22 + C12 + C42 = 1 + 0 + 6 = 7
        return sum(x * (x - 1) // 2 for x in kcnt)
                