# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp=head
        size=0
        while tmp:
            size+=1
            tmp=tmp.next
        
        if size==n:
            return head.next

        newN=size-n
        tmp=head
        prev=None
        while newN>0:
            prev=tmp
            tmp=tmp.next
            newN-=1
        prev.next=tmp.next

        return head


        
        