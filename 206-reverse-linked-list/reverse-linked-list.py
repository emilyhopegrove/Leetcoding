# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        previous, current = None, head
#while there is a current that is existing (not None)
        while current:

            temporary_container = current.next
            current.next = previous
            previous = current
            current = temporary_container

        return previous
