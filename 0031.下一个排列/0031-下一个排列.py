class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #i �����nums��β��ǰ�������е�ͷ�� j��������������nums[i - 1]�����С��Ԫ��
        
        l = len(nums)
        for i in range(l - 1, -1, -1):
            if nums[i - 1] < nums[i]:# �ҵ�����Ҫ��i
                break
        
        if i == 0: # ����ǰ��������һ����������У����巭ת����
            nums[:] = nums[::-1]
            return nums
        
        for j in range(l - 1, i - 1, -1):
            if nums[j] > nums[i - 1]: #�ҵ�����Ҫ��j
                break

        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = nums[i:][::-1]
        return nums