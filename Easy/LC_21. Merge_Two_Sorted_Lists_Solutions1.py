#LeetCode 21. Merge Two Sorted Lists
# Easy

#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

#Return the head of the merged linked list.


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dum = cur = ListNode()    
        while list1 and list2:
            if list2.val > list1.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
                     
            
        return dum.next