class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next

        return slow