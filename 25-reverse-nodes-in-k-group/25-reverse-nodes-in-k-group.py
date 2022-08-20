# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None :
            return head
        l = 0
        cur = head
        while cur:
            cur = cur.next
            l += 1
        pairs = l//k
        pairs_comp = 0
        count = 0
        dummy = ListNode(0,head)
        cur = dummy.next
        prev, tail = dummy, dummy
        while pairs_comp != pairs:
            if count == k:
                if cur is None:
                    return dummy.next
                node = cur
                cur = cur.next
                prev = tail
                node.next = prev.next
                prev.next = node
                tail = node
                count = 1
                pairs_comp += 1
            else:
                count += 1
                node = cur
                cur = cur.next
                node.next = prev.next
                prev.next = node
                if tail == dummy:
                    tail = node
                    tail.next = None
        tail.next = cur
        return dummy.next
            