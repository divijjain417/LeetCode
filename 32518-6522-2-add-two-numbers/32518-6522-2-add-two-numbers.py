# Definition for singly-linked list.
#class ListNode(object):
     #def __init__(self, val=0, next=None):
         #self.val = val
         #self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        numberOfDigits = 0
        carryover = 0
        final = result = ListNode(0)
        while (l1 or l2 or carryover) :
            total = carryover
            if l1: 
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carryover = total // 10 
            num = total % 10
            
            result.next = ListNode(num)
            result = result.next

        return final.next
        