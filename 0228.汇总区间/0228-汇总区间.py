class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums
        start, end = nums[0], nums[0]
        
        res = list()
        for i, x in enumerate(nums):
            if i == 0:
                continue
            
            if x == end + 1:#��������
                end = x
            elif x != end + 1: #�ж��� ���������һ������
                # print i, x, start, end
                temp = ""
                if start == end: #ֻ��һ����
                    temp += str(end)
                else:
                    temp += str(start) + "->" + str(end)
                res.append(temp)
                
                start, end = x, x
                
            if i == len(nums) - 1:
                temp = ""
                if start == end: #ֻ��һ����
                    temp += str(end)
                else:
                    temp += str(start) + "->" + str(end)
                res.append(temp)     
                
        # print start, end
        return res if len(nums) > 1 else [str(nums[0])]
            