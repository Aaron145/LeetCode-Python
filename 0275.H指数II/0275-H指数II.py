class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        lo, hi = 0, l - 1
        res = 0
        while(lo <= hi):
            mid = lo + (hi - lo) // 2
            cnt = l - mid #����mid�����ұ߻��е�Ԫ�ظ���
            if citations[mid] >= cnt: 
                res = cnt
                hi = mid -1
            else:
                lo = mid + 1
        return res
                