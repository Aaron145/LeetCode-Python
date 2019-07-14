class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        res = []
        left = [] #���û����arr2����ֹ�������
        set2 = set(arr2) #��arr2ת��set���ò��ҵ�ʱ�临�ӶȽ��͵�O(1)
       
        dic = defaultdict(int) #��¼arr1�����ֳ��ֵ�Ƶ��
        for num in arr1:
            if num in set2:
                dic[num] += 1
            else:
                left.append(num)

        for num in arr2:
            res += [num] * dic[num]

        left.sort() #������ĿҪ���û���ֹ���Ԫ������
        return res + left
            