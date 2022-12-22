"""
19. Remove Nth Node From End of List


Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x = 0
        i = 0
        cur = head
        cur2 = head
        while cur is not None:
            cur = cur.next
            x += 1
        
        if x == 1:
            head = None
            return head
        if x == n:
            cur2 = cur2.next
            return cur2
            
            
        print(x)
        while cur2 is not None:
            
            if i+1 == x - n: 
                cur2.next = cur2.next.next
            cur2 = cur2.next
            i += 1   
            
        return head