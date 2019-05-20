class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ���ڴ���1~n֮������������Ƿŵ�nums[i - 1]��λ����
        
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                
        for i, x in enumerate(nums):
            if x != i + 1:
                return i + 1
        
        return len(nums) + 1