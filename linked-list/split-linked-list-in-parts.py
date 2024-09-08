# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ret = []
        kcopy = k
        count = 0
        n = head
        while n is not None:
            n = n.next
            count+=1
        print(count/k)
        lnode = head
        while count>0:
            r = count//k + 1
            if count%k==0:
                r = count//k
            currnode = ListNode(lnode.val)
            ret.append(currnode)
            print(ret)
            print(r)
            for i in range(r-1):
                if currnode is None:
                    break
                if lnode.next is None:
                    break
                currnode.next = ListNode(lnode.next.val)
                lnode = lnode.next
                currnode = currnode.next
            lnode = lnode.next
            # if currnode is not None:
            #     currnode.next = None
            print(currnode.val)
            count-=r
            k-=1
        
        while len(ret)<kcopy:
            ret.append(None)

        return ret
        