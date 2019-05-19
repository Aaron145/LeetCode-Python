from heapq import *
class MedianFinder(object):
# ά�������ѣ�һ���󶥶ѣ�һ��С���ѣ�С����������ȴ󶥶��������Ҫ�� 
# ���������Ǳ�ڵ���λ����������size��ͬ��������������λ�����������Ѷ�֮�ͳ���2
# ���ֻ��һ����λ�����Ϳ�size��С���Ǹ��ѵĶѶ�
# ����½���������С���ѵ���ҪС���Ͱ�������󶥶�
# ����½���������С���ѵ���Ҫ�󣬾Ͱ�������С����
# ���������ѣ�ʹ��size �����Ϊ1
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_h = list()
        self.min_h = list()
        heapify(self.max_h)
        heapify(self.min_h)
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heappush(self.min_h, num)
        heappush(self.max_h, -heappop(self.min_h))
        if len(self.max_h) > len(self.min_h):
            heappush(self.min_h, -heappop(self.max_h))

    def findMedian(self):
        """
        :rtype: float
        """
        max_len = len(self.max_h)
        min_len = len(self.min_h)
        if max_len == min_len: #��������ѡ��λ��
            return (self.min_h[0] + -self.max_h[0]) / 2.
        else:#С���ѵ�size һ�� >= �󶥶ѵ�size�����Դ𰸾���С���ѵĶѶ�
            return self.min_h[0] / 1.
            
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mf = MedianFinder()
        for num in nums1:
            mf.addNum(num)
        for num in nums2:
            mf.addNum(num)
        return mf.findMedian()