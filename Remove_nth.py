# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        temp=head
        temp1=head
        dist=0
        while temp and temp.next:
            print(temp1.val,temp.val,dist)
            if dist>=n: 
                temp1=temp1.next
            temp=temp.next
            dist+=1
        if dist>=n:
            temp1.next=temp1.next.next
        else:
            head=temp1.next
        return head
