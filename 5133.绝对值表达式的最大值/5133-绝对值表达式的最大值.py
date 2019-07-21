class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        record = [-2 ** 31] * 8
        
        for i in range(len(arr1)):
            for k in range(8): #���ɰ��ֿ��ܵĽ��
                t = 0
                if k & 1:
                    t += arr1[i]
                else:
                    t -= arr1[i]
                if k & 2:
                    t += arr2[i]
                else:
                    t -= arr2[i]
                if k & 4:
                    t += i
                else:
                    t -= i
                # print k, t
                record[k] = max(record[k], t)
        # print record
        res = 0    
        for k in range(8):
            # print k, ~k
            res = max(res, record[k] + record[-k-1]) #��һ������һ��ڶ���͵����ڶ������֮��һ����������ʽ��
        return res
                
            