# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        if not root:
            return []
        to_delete = set(to_delete)
        
        res = []
        
        self.roots = []
        if root.val not in to_delete:
            self.roots = [root]
        else: #��������ڵ㶼Ҫɾ��
            if root.left and root.left.val not in to_delete:
                self.roots += [root.left]
            if root.right and root.right.val not in to_delete:
                self.roots += [root.right]
        
        def dfs(node):
            if not node:
                return

            if node.left and node.left.val in to_delete:  #��ڵ�Ҫɾ
                dfs(node.left)
                if node.left.left: #��ڵ����ڵ㻹�ڣ�����Ҫɾ
                    self.roots += [node.left.left]
                if node.left.right: #��ڵ���ҽڵ㻹�ڣ�����Ҫɾ
                    self.roots += [node.left.right]
                
                node.left = None
                
            if node.right and node.right.val in to_delete:#�ҽڵ�Ҫɾ
                dfs(node.right)
                if node.right.left: #�ҽڵ����ڵ㻹�ڣ�����Ҫɾ
                    self.roots += [node.right.left]
                if node.right.right: #�ҽڵ���ҽڵ㻹�ڣ�����Ҫɾ
                    self.roots += [node.right.right]
                
                node.right = None

            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return self.roots
            
            