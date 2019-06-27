# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        pre = head #preʼ��ָ���������������һ���ڵ�
        cur = head.next #curʼ��ָ��δ��������ĵ�һ���ڵ�
        while cur:
            tail = cur.next
            pre.next = tail  #��cur����ڵ��ó���
            
            p = dummy
            while p.next and p.next.val < cur.val: #�ҵ������λ��
                p = p.next
                
            cur.next = p.next #��cur���뵽p��p.next֮��
            p.next = cur
            cur = tail
            
            if p == pre:#����ղ��뵽�������������ĩβ
                pre = pre.next #��ô�͸���pre
        return dummy.next