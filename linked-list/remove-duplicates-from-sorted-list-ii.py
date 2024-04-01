# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        prev = dummyNode
        curr = head
        prev.next = curr
        if head==None:
            return head
        if head.next != None:
            next = head.next
        else:
            return head
        while(next!=None):
            if curr.val != next.val:
                prev = curr
                curr = next
                next = next.next
            else:
                #move next till you find a value that differs curr
                while(next.val==curr.val):
                    if next.next!=None:
                        next = next.next
                    else:
                        next = None
                        prev.next = None
                        break
                #found a next that is diff than curr
                prev.next = next
                curr = next
                if next!=None:
                    next = next.next
        return dummyNode.next
        
        