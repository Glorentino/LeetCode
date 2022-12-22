"""
328. Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        oddLL = head
        evenLL = head.next
        evenHead = evenLL
        while evenLL and evenLL.next:
            oddLL.next = evenLL.next
            oddLL = oddLL.next
            evenLL.next = oddLL.next
            evenLL = evenLL.next
        oddLL.next = evenHead
        return head