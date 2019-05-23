# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        if not root or (not root.left and not root.right):
            return root
        
        #�Ȱ�����������ֱ
        self.flatten(root.left)
        self.flatten(root.right)
        
        tmp = root.right #����ֱ������������һ��
        
        root.right = root.left #����ֱ���������ŵ��ұ�
        root.left = None #�ǵð��������ÿ�
        while(root.right): #�ҵ����������������һ��node
            root = root.right
        root.right = tmp #����ֱ��ԭ��������������ȥ
        