# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev=head
        if prev==None:
            return head
        temp=prev.next
        while temp!=None:
            if prev.val==temp.val:
                temp=temp.next
                prev.next=temp
            else:
                temp=temp.next
                prev=prev.next
        return head
