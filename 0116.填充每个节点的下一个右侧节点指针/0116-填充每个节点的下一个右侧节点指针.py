"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        #���ų�������Ҫ��������
        if not root or (not root.left and not root.right):
            return root
        
        #ĳһ���ڵ�����ӵ�nextһ����ָ������ڵ���Һ���
        root.left.next = root.right
        
        #��ĳһ���ڵ��next��Ϊ�յ�ʱ������ڵ���Һ��ӵ�nextһ����ָ��ýڵ�next��left
        if root.next:
            root.right.next = root.next.left
        
        #�ݹ鴦����һ��
        self.connect(root.left)
        self.connect(root.right)
  
        return root
                