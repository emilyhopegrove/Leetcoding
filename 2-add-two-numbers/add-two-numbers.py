# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        # Initializes a new node with a given value and a reference to the next node.
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Create a dummy head node to simplify the handling of the edge case for the head of the result list.
        dummy_head = ListNode(0)
        # This 'current' pointer will be used to add new nodes to the result list.
        current = dummy_head
        # Carry will hold any carry-over value from adding two digits.
        carry = 0

        # Continue looping as long as there is a node in either list or there is a carry value.
        while l1 is not None or l2 is not None or carry:
            # Get the value from the current node of l1, or 0 if l1 is None.
            val1 = (l1.val if l1 else 0)
            # Get the value from the current node of l2, or 0 if l2 is None.
            val2 = (l2.val if l2 else 0)
            # Add the values from the two lists and any carry from the previous addition.
            sum_ = val1 + val2 + carry

            # Calculate the new carry for the next addition (1 if sum is 10 or more, otherwise 0).
            carry = sum_ // 10
            # The actual digit to store in the current node (remainder of sum divided by 10).
            sum_ = sum_ % 10
            # Create a new node with the sum and link it to the current node.
            current.next = ListNode(sum_)

            # Move the 'current' pointer to the newly created node.
            current = current.next
            # Advance l1 and l2 to their next nodes if they exist, otherwise, keep them as None.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Since dummy_head is a placeholder, we return dummy_head.next as the head of the actual result list.
        return dummy_head.next
