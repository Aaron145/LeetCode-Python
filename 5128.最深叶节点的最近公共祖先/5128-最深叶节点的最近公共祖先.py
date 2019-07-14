# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        # print inorder(root)
        if not root or (not root.left and not root.right):
            return root
        
        dic = {}
        def depth(node, tmp):
            if not node:
                return
            dic[node] = tmp + 1
            depth(node.left, tmp + 1)
            depth(node.right, tmp + 1)
            
        depth(root, 0)
        # print dic
        l = []
        max_depth = max(dic.values())
        for key, val in dic.items():
            if val == max_depth:
                l.append(key)
                
        if len(l) == 1:
            return l[0]
        # print l
        tmpAncestor = None
        if len(l) >= 2:
            tmpAncestor = self.lowestCommonAncestor(root, l[0], l[1])
        for i in range(2, len(l), 1):
            tmpAncestor = self.lowestCommonAncestor(root, tmpAncestor, l[i])
        return tmpAncestor
            
        
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if not root or root == p or root == q:
            return root
        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            
            if left and right: #һ������������һ����������
                return root
            elif left:#����������
                return left
            elif right:#����������
                return right
            else:
                return