# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1,-1]

        first,last=-1,-1
        min_dist=float("inf")
        pos=1
        prev,curr,nxt=head,head.next,head.next.next

        while curr and nxt:
            is_critical=(
                (curr.val>prev.val and curr.val>nxt.val)
                or 
                (curr.val<prev.val and curr.val<nxt.val)
            )

            if is_critical:
                if first==-1:
                    first=pos
                else:
                    min_dist=min(min_dist,pos-last)

                last=pos

            prev,curr,nxt=curr,nxt,nxt.next
            pos+=1

        if first==-1 or first==last:
            return [-1,-1]

        max_dist=last-first

        return [min_dist,max_dist]