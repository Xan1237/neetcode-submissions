# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        # Use dummy head for returning
        newHead = ListNode(0, None)
        newList = newHead

        # Keep track of carry between two numbers
        carry = 0

        # Break when we are at the end of both numbers
        while(l1 or l2):
            newVal = 0

            # If the number is over we just say its 0
            if l1:
                newVal += l1.val
                l1 = l1.next
            if l2:
                newVal += l2.val
                l2 = l2.next
        
            newVal += carry

            # Calcualte the carry and new node value
            carry = (newVal // 10)
            newNode = ListNode((newVal % 10), None)

            # append the value to the new number
            newList.next = newNode
            newList = newList.next

        # If we still had a cary at the end of both numbers
        if carry != 0:
            newList.next = ListNode(1, None)
            
        return newHead.next





        