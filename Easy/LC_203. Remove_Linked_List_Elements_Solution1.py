"""
203. Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""

def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

    dummyNode = ListNode(0)
    dummyNode.next = head

    prev, curr = dummyNode, head

    while curr: 
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummyNode.next
