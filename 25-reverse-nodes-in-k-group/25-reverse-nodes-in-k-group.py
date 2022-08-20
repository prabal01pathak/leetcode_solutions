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
        dummy = ListNode(0)
        cur = head
        prev, tail = dummy, dummy
        while pairs_comp != pairs:
            if count == k:
                if cur is None:
                    return dummy.next
                node = ListNode(cur.val)
                prev = tail
                node.next = prev.next
                prev.next = node
                tail = node
                cur = cur.next
                count = 1
                pairs_comp += 1
            else:
                count += 1
                node = ListNode(cur.val)
                node.next = prev.next
                prev.next = node
                cur = cur.next
                if tail == dummy:
                    tail = node
        tail.next = cur
        return dummy.next
            