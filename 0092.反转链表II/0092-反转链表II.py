# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # ���ҵ�m ~ n��һ�Σ���ת��������ȥ
        if m == n:
            return head
        cnt = 1
        pre_m, pn = None, None
        node = head
        while(cnt < n):
            # print node.val, cnt
            if cnt == m - 1:
                pre_m = node
            node, cnt = node.next, cnt + 1
        pn = node
        if pn:
            nextn = pn.next
            pn.next = None
        else:
            nextn = None
        # print pre_m.val, nextn.val
         
        if pre_m is None: #��1��ʼ
            head = self.reverseList(head)
            newhead = head
            while(head.next):
                head = head.next
            head.next = nextn
            return newhead
        else:
            pre_m.next = self.reverseList(pre_m.next)
            newhead = head
            while(head.next):
                head = head.next
            head.next = nextn
            return newhead
        
            
            

        
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        tmp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tmp