# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        for i in lists:
            cur = i
            while cur:
                l.append(cur.val)
                cur = cur.next
        l.sort()
        dummy = ListNode(0)
        cur = dummy
        for i in l:
            node = ListNode(i)
            cur.next = node
            cur = cur.next
        return dummy.next