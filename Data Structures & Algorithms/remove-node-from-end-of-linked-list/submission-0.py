# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        right = head
        left = dummy

        #this gets the right pointer at n from the start
        while n > 0:
            right = right.next
            n -= 1

        # this puts left n nodes from the end
        while right:
            right = right.next
            left = left.next

        #removes the nth node from the end
        left.next = left.next.next

        # We return dummy.next just in case head is deleted
        return dummy.next
