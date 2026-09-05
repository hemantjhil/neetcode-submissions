# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        # reverse the second part
        second=slow.next
        prev=slow.next=None
        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp
        
        #merge two parts (first half and second reversed)
        first,second=head,prev
        while second:
            first1,second1=first.next,second.next
            first.next=second
            second.next=first1
            first,second=first1,second1
            
        